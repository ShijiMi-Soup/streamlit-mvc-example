import pandas as pd

class PostHandler:
    """投稿データの管理をするクラス"""

    db_path = "database/posts.csv"
    """データベースファイル (csv) へのパス"""

    def read(self):
        """データベースからデータを読む"""

        df = pd.read_csv(self.db_path)
        return df
    
    def add(self, content):
        """データベースにデータを追加する"""

        posts = self.read()

        if len(posts) == 0:
            post_id = 0
        else:
            last_row = posts.iloc[len(posts) - 1]
            post_id = last_row["PostId"] + 1

        posts.loc[len(posts)] = [post_id, content]
        posts.to_csv(self.db_path, index=False)
    
    def update(self, post_id, content):
        """データベースのデータを更新する"""

        posts = self.read()

        update_idx = -1
        for index, row in posts.iterrows():
            if row["PostId"] == post_id:
                update_idx = index
                break
        
        if update_idx >= 0:
            posts.loc[update_idx, "Content"] = content
            posts.to_csv(self.db_path, index=False)

    def delete(self, post_id):
        """データベースのデータを削除する"""

        posts = self.read()

        delete_idx = -1
        for index, row in posts.iterrows():
            if row["PostId"] == post_id:
                delete_idx = index
                break
        
        if delete_idx >= 0:
            posts = posts.drop(delete_idx)
            posts.to_csv(self.db_path, index=False)