# Created by: kok-s0s
# Last Modified at: Wed Mar 12 16:43:47 2025
# File Name: unit_converter.py

import math


def deg_to_rad(degrees):
    """角度转换为弧度"""
    return degrees * math.pi / 180.0


def rad_to_deg(radians):
    """弧度转换为角度"""
    return radians * 180.0 / math.pi


def mm_to_millimeter(mm):
    """毫米转换为米"""
    return mm / 1000.0


def meter_to_mm(meters):
    """米转换为毫米"""
    return meters * 1000.0


def cart_to_polar(x, y):
    """笛卡尔坐标转换为极坐标"""
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    return r, rad_to_deg(theta)


def polar_to_cart(r, theta):
    """极坐标转换为笛卡尔坐标"""
    theta_rad = deg_to_rad(theta)
    x = r * math.cos(theta_rad)
    y = r * math.sin(theta_rad)
    return x, y


def rpm_to_rad_per_sec(rpm):
    """转速（RPM）转换为弧度每秒"""
    return rpm * 2 * math.pi / 60.0


def rad_per_sec_to_rpm(rad_per_sec):
    """弧度每秒转换为转速（RPM）"""
    return rad_per_sec * 60.0 / (2 * math.pi)


def velocity_mm_per_s_to_m_per_s(velocity):
    """速度从毫米/秒转换为米/秒"""
    return velocity / 1000.0


def velocity_m_per_s_to_mm_per_s(velocity):
    """速度从米/秒转换为毫米/秒"""
    return velocity * 1000.0


def force_N_to_kg(force_N):
    """牛顿转换为千克力（假设重力加速度为 9.81 m/s^2）"""
    return force_N / 9.81


def kg_to_force_N(mass_kg):
    """千克力转换为牛顿（假设重力加速度为 9.81 m/s^2）"""
    return mass_kg * 9.81


def interactive_menu():
    """交互式终端菜单"""
    options = {
        "1": ("角度转换为弧度", deg_to_rad),
        "2": ("弧度转换为角度", rad_to_deg),
        "3": ("毫米转换为米", mm_to_millimeter),
        "4": ("米转换为毫米", meter_to_mm),
        "5": ("笛卡尔坐标转换为极坐标", cart_to_polar),
        "6": ("极坐标转换为笛卡尔坐标", polar_to_cart),
        "7": ("转速（RPM）转换为弧度每秒", rpm_to_rad_per_sec),
        "8": ("弧度每秒转换为转速（RPM）", rad_per_sec_to_rpm),
        "9": ("速度从毫米/秒转换为米/秒", velocity_mm_per_s_to_m_per_s),
        "10": ("速度从米/秒转换为毫米/秒", velocity_m_per_s_to_mm_per_s),
        "11": ("牛顿转换为千克力", force_N_to_kg),
        "12": ("千克力转换为牛顿", kg_to_force_N),
        "q": ("退出", None),
    }

    while True:
        print("\n请选择转换类型:")
        for key, (desc, _) in options.items():
            print(f"{key}. {desc}")

        choice = input("请输入选项编号: ")
        if choice == "q":
            print("退出程序。")
            break

        if choice in options:
            desc, func = options[choice]
            if func:
                if choice in ["5", "6"]:
                    x = float(input("输入 x/r: "))
                    y = float(input("输入 y/θ（角度）: "))
                    print(f"结果: {func(x, y)}")
                else:
                    value = float(input("输入数值: "))
                    print(f"结果: {func(value)}")
        else:
            print("无效输入，请重新选择。")


if __name__ == "__main__":
    interactive_menu()
