def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    return weight_kg / (height_m ** 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "體重過輕"
    elif bmi < 24:
        return "正常體重"
    elif bmi < 27:
        return "體重過重"
    elif bmi < 30:
        return "輕度肥胖"
    elif bmi < 35:
        return "中度肥胖"
    else:
        return "重度肥胖"

def main():
    print("=== BMI 計算機 ===")

    while True:
        try:
            weight = float(input("請輸入體重 (公斤): "))
            height = float(input("請輸入身高 (公分): "))

            if weight <= 0 or height <= 0:
                print("體重和身高必須大於 0，請重新輸入。\n")
                continue

            bmi = calculate_bmi(weight, height)
            category = get_bmi_category(bmi)

            print(f"\nBMI 值：{bmi:.2f}")
            print(f"體重狀態：{category}")
            print("\n--- BMI 對照表 ---")
            print("< 18.5   體重過輕")
            print("18.5–24  正常體重")
            print("24–27    體重過重")
            print("27–30    輕度肥胖")
            print("30–35    中度肥胖")
            print(">= 35    重度肥胖")
            break
        except ValueError:
            print("請輸入有效的數字。\n")

if __name__ == "__main__":
    main()
