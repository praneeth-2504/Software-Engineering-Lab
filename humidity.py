
# W= 0.5T^2 - 0.2H + 0.1W - 15
# W= weather prediction (o/p)
# T= Temperature(i/p)
# H= Humidity(i/p)
# W= wind Speed(i/p)

#if w>300 predict as sunny
#if 200<w<=300 predict as cloudy
#if 100<w<=200 predict as rainy
#of w<=100 prredcit as stormy


#lineaer process
# dynamic

def predict_weather():

    H = float(input("Humidity: "))
    T = float(input("Temperature: "))
    Wi = float(input("Wind speed: "))

    W = 0.5 * T**2 - 0.2 * H + 0.1 * Wi - 15

    if W > 300:
        return 'Sunny'
    elif 200 < W <= 300:
        return 'Cloudy'
    elif 100 < W <= 200:
        return 'Rainy'
    else:
        return 'Stormy'

print(predict_weather())




# static and user given multiple inputs

class Test_class:
    def predict(condition):
        if condition > 50:
            return "Sunny"
        else:
            return "Rainy"


Test_cases = [[20, 70, 15], [30, 60, 10], [20, 80, 5], [15, 90, 25]]
outputs = ["Rainy", "Sunny", "Rainy", "Stormy"]

predicted_outputs = []
for conditions in Test_cases:
    predicted_outputs.append(Test_class.predict(conditions[0]))

print("Expected outputs: ", outputs)
print("Predicted outputs: ", predicted_outputs)

if outputs == predicted_outputs:
    print("All tests passed")
else:
    print("Not all tests passed")




#08-12-23

# write a program in python
# 1.Variable values static
# 2.Variable values dynamic
# 3.User given multiple inputs
# 4.Reading values from files


# 4th
def predict_weather_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

            H = float(lines[0].strip())
            T = float(lines[1].strip())
            Wi = float(lines[2].strip())

            W = 0.5 * T**2 - 0.2 * H + 0.1 * Wi - 15

            if W > 300:
                return 'Sunny'
            elif 200 < W <= 300:
                return 'Cloudy'
            elif 100 < W <= 200:
                return 'Rainy'
            else:
                return 'Stormy'
    except FileNotFoundError:
        return "File not found."

file_path = "/content/filename.txt"
result = predict_weather_from_file(file_path)
print(result)
