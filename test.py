
dic = [
  {
    "Gender": "Male",
    "HeightCm": 171,
    "WeightKg": 96
  },
  {
    "Gender": "Male",
    "HeightCm": 161,
    "WeightKg": 85
  },
  {
    "Gender": "Male",
    "HeightCm": 180,
    "WeightKg": 77
  },
  {
    "Gender": "Female",
    "HeightCm": 166,
    "WeightKg": 62
  },
  {
    "Gender": "Female",
    "HeightCm": 150,
    "WeightKg": 70
  },
  {
    "Gender": "Female",
    "HeightCm": 167,
    "WeightKg": 82
  }
]





def BMI(a):
	#BMI(kg/m​ ) = mass(kg) / height(m)
	bmi_li = []
	for i in a:
		bmi_li.append(i["WeightKg"]/((i["HeightCm"]/100)*(i["HeightCm"]/100)))
	for i in bmi_li:
		if i <=18.4:
			print("Under weight --> Malnutrition risk -->",i)
		elif i <=24.9:
			print("Normal weight  -->  Low risk	-->",i)
		elif i <=29.9:
			print("Overweight  -->  Enhanced risk	-->",i)
		elif i <=34.9:
			print("Moderately obese  --> Medium risk	-->",i)
		elif i <=39.9:
			print("Severely obese  -->  High risk	-->",i)
		elif  i >=40.0:
			print("Veryseverely obese  -->  Very high risk	-->",i)


BMI(dic)		


