class Student :
    # メソッドは渡したい引数がない場合でも必ず引数が必要になる
    # 渡したい引数がない場合は「self」と記述
    # def avg(self):
    #     print((80 + 70)/2)
    
    # 引数が１つの場合
    # def avg(self, arg00):
    #     print((80 + 70)/2)

    # コンストラクタ(初期化メソッド)の作り方
    def __init__(self, name):
        self.name = name

    def avg(self, math, english):
        print((math + english)/2)

    

# クラスを使えるようにするためにインスタンス化    
a001 = Student("ueda")

# アトリビュート
a001.name = "sato"
print(a001.name)

a002 = Student("tanaka")
print(a002.name)