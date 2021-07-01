import sqlite3

class Database:

    def __init__(self):

        self.conn = sqlite3.connect('muxdb.sqlite', check_same_thread = False)

    def setup(self):

        cmd = """CREATE TABLE IF NOT EXISTS muxbot(
        user_id INT,
        vid_name TEXT,
        sub_name TEXT,
        filename TEXT
        );"""

        self.conn.execute(cmd)
        self.conn.commit()

    def put_video(self, user_id, vid_name, filename):

        ins_cmd = 'INSERT INTO muxbot VALUES (?,?,?,?);'
        srch_cmd = f'SELECT * FROM muxbot WHERE user_id={user_id};'
        up_cmd = f'UPDATE muxbot SET vid_name="{vid_name}", filename="{filename}" WHERE user_id={user_id};'
        data = (user_id, vid_name, None, filename)
        res = self.conn.execute(srch_cmd).fetchone()
        if res:
            self.conn.execute(up_cmd)
            self.conn.commit()
        else :
            self.conn.execute(ins_cmd,data)
            self.conn.commit()

    def put_sub(self,user_id,sub_name) :

        ins_cmd = 'INSERT INTO muxbot VALUES (?,?,?,?);'
        srch_cmd = f'SELECT * FROM muxbot WHERE user_id={user_id};'
        up_cmd = f'UPDATE muxbot SET sub_name="{sub_name}" WHERE user_id={user_id};'
        data = (user_id,None,sub_name,None)

        res = self.conn.execute(srch_cmd).fetchone()
        if res :
            self.conn.execute(up_cmd)
            self.conn.commit()
        else :
            self.conn.execute(ins_cmd,data)
            self.conn.commit()

    def check_sub(self,user_id) :

        srch_cmd = f'SELECT * FROM muxbot WHERE user_id={user_id};'

        res = self.conn.execute(srch_cmd).fetchone()
        if res :

            sub_file = res[2]
            if sub_file :
                return True
            else :
                return False

        else :
            return False

    def check_video(self,user_id) :

        srch_cmd = f'SELECT * FROM muxbot WHERE user_id={user_id};'
        res = self.conn.execute(srch_cmd).fetchone()
        if res :
            vid_file = res[1]
            if vid_file :
                return True
            else :
                return False
        else :
            return False

    def get_vid_filename(self, user_id) :

        cmd = f'SELECT * FROM muxbot WHERE user_id={user_id};'
        res = self.conn.execute(cmd).fetchone()
        if res :
            return res[1]
        else :
            return False

    def get_sub_filename(self, user_id) :

        cmd = f'SELECT * FROM muxbot WHERE user_id={user_id};'
        res = self.conn.execute(cmd).fetchone()
        if res :
            return res[2]
        else :
            return False

    def get_filename(self, user_id) :

        cmd = f'SELECT * FROM muxbot WHERE user_id={user_id};'
        res = self.conn.execute(cmd).fetchone()
        if res :
            return res[3]
        else :
            return False

    def erase(self,user_id) :

        erase_cmd = f'DELETE FROM muxbot WHERE user_id={user_id} ;'

        try :
            self.conn.execute(erase_cmd)
            self.conn.commit()
            return True
        except :
            return False
