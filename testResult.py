class Student:
    def __init__(self, name, arg01, arg02, arg03, arg04, arg05):
        self.name = name
        print("名前 : " + self.name)
        self.judge(arg01, arg02, arg03, arg04, arg05)
    
    # 5教科の平均点を計算する
    def calculateAvg(selt, arg01, arg02, arg03, arg04, arg05):
        return (arg01 + arg02 +  arg03 + arg04 + arg05)/5
    
    # 平均点以上だったら合格("passed")、平均点以下なら不合格("failed")を表示する
    def judge(self, arg01, arg02, arg03, arg04, arg05):
        test = [arg01, arg02, arg03, arg04, arg05]
        subject = ["国語", "数学", "英語", "理科", "社会"]
        for i in range(5):
            if test[i] >= self.calculateAvg(arg01, arg02, arg03, arg04, arg05):
                print(subject[i] + " : passed")
            else:
                print(subject[i] + " : failed")


a001 = Student("sato", 70, 80, 80, 60, 90)