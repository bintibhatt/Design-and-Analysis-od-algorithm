
    for i in range(len(data)):
        for j in range(len(data), 0 , -1):
            if data[j] < data[j-1]:
                t = data[j]
                data[j] = data[j-1]
                data[j-1] = data[j]
print(data)