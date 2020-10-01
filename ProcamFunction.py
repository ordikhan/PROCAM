class Procam:

    def __init__(self, age, diabetes, smoker, bloodPersore, Hdl, familyHistory, Ldl, triglycerides):
        self.age = age
        self.diabetes = diabetes
        self.smoker = smoker
        self.bloodPersore = bloodPersore
        self.Hdl = Hdl
        self.familyHistory = familyHistory
        self.Ldl = Ldl
        self.triglycerides = triglycerides

    def ProcamRisk(self):
        RiskScore = []
        # AGE
        if self.age <= 39:
            RiskScore.append(0)
        elif 39 < self.age <= 44:
            RiskScore.append(6)
        elif 44 < self.age <= 49:
            RiskScore.append(11)
        elif 49 < self.age <= 54:
            RiskScore.append(16)
        elif 54 < self.age <= 59:
            RiskScore.append(21)
        elif 59 < self.age:
            RiskScore.append(26)
        # diabetes
        if self.diabetes == 0:
            RiskScore.append(6)
        else:
            RiskScore.append(0)
        # smoker
        if self.smoker == 1:
            RiskScore.append(8)
        else:
            RiskScore.append(0)
        # familyHistory
        if self.familyHistory == 1:
            RiskScore.append(4)
        else:
            RiskScore.append(0)
        # LDL
        if self.Ldl <= 100:
            RiskScore.append(0)
        elif 100 < self.Ldl <= 129:
            RiskScore.append(5)
        elif 129 < self.Ldl <= 159:
            RiskScore.append(10)
        elif 159 < self.Ldl <= 189:
            RiskScore.append(14)
        elif 189 < self.Ldl:
            RiskScore.append(20)
        # HDL
        if self.Hdl <= 35:
            RiskScore.append(11)
        elif 35 < self.Hdl <= 44:
            RiskScore.append(8)
        elif 44 < self.Hdl <= 54:
            RiskScore.append(5)
        elif 54 < self.Hdl:
            RiskScore.append(0)
        # triglycerides
        if self.triglycerides <= 100:
            RiskScore.append(0)
        elif 100 < self.triglycerides <= 149:
            RiskScore.append(2)
        elif 149 < self.triglycerides <= 199:
            RiskScore.append(3)
        elif 199 < self.triglycerides:
            RiskScore.append(4)
        # BloodPersore
        if self.bloodPersore <= 120:
            RiskScore.append(0)
        elif 120 < self.bloodPersore <= 129:
            RiskScore.append(2)
        elif 129 < self.bloodPersore <= 139:
            RiskScore.append(3)
        elif 139 < self.bloodPersore <= 159:
            RiskScore.append(5)
        elif 159 < self.bloodPersore:
            RiskScore.append(8)

        TotalScore = sum(RiskScore)
        Score = []
        if TotalScore <= 20:
            Score.append('< 1 %')
        elif 20 < TotalScore <= 28:
            Score.append('< 2 %')
        elif 28 < TotalScore <= 37:
            Score.append(' 5 %')
        elif 37 < TotalScore <= 44:
            Score.append(' 10 %')
        elif 44 < TotalScore <= 53:
            Score.append(' 20 %')
        elif 53 < TotalScore <= 61:
            Score.append('< 40 %')
        elif TotalScore > 61:
            Score.append('> 40 %')

        return str(Score[0])
