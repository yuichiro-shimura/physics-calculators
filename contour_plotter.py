import numpy as np
import matplotlib.pyplot as plt

# データ生成（例：数値流体解析の結果）
x = np.linspace(0, 10, 100)
y = np.sin(x) + 0.1 * np.random.randn(100)

# コンターグラフの作成
plt.figure(figsize=(8, 6))
plt.contourf(x.reshape(10, 10), y.reshape(10, 10), levels=20, cmap='viridis')
plt.colorbar(label='値')

# 軸の設定
plt.xlabel('X軸')
plt.ylabel('Y軸')

# グリッドの表示
plt.grid(True)

# タイトルと保存
plt.title('2D コンターグラフ')
#plt.savefig('contour_plot.png', dpi=300, bbox_inches='tight')
plt.show()