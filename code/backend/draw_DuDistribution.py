import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import numpy as np
import random


def validate_data(degrees, frequencies):
    """
    验证输入数据的合法性。
    """
    if len(degrees) != len(frequencies):
        raise ValueError("degrees和frequencies的长度不相等")
    if not degrees or any(degrees[i] >= degrees[i + 1] for i in range(len(degrees) - 1)):
        raise ValueError("degrees必须是非降序且非空")
    return degrees, frequencies


def generate_smooth_data(degrees, frequencies):
    """
    使用spline插值函数使曲线平滑。
    """
    x_smooth = np.linspace(min(degrees), max(degrees), 100)
    y_smooth = make_interp_spline(degrees, frequencies)(x_smooth)
    return x_smooth, y_smooth


def plot_distribution(x_smooth, y_smooth):
    """
    绘制度分布曲线。
    """
    plt.plot(x_smooth, y_smooth, '-', linewidth=1)
    plt.legend()
    plt.show()


def generate_lists():
    degrees = list(range(1, 51))  # 生成从1到50的整数列表
    frequencies = [5 / degree + 5.6 for degree in degrees]  # 根据公式计算频率值并生成列表
    # 在frequencies中使用Random函数加入适当扰动
    for i in range(100):
        frequencies[random.randint(0, 49)] += random.uniform(-0.05, 0.1)
    return degrees, frequencies


def main():
    # 函数数据（假设，实际应根据您的数据生成）
    degrees, frequencies = generate_lists()


    try:
        validated_degrees, validated_frequencies = validate_data(degrees, frequencies)
        x_smooth, y_smooth = generate_smooth_data(validated_degrees, validated_frequencies)
        plot_distribution(x_smooth, y_smooth)
    except ValueError as e:
        print(f"数据验证失败: {e}")


if __name__ == "__main__":
    main()
