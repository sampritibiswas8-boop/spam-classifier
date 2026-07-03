import joblib

# load model
model = joblib.load("model/spam_model.pkl")

print("\n📩 Spam Classifier Running")
print("Type 'exit' to stop\n")

while True:
    msg = input("Enter message: ")

    if msg.lower() == "exit":
        break

    pred = model.predict([msg])[0]

    if pred == 1:
        print("🚨 Spam\n")
    else:
        print("✅ Not Spam\n")