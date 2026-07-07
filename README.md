# 房价预测神经网络

## 项目简介
基于 TensorFlow/Keras 的全连接神经网络实现房价预测，使用 Kaggle House Prices 数据集（1460行 x 81列），包含完整的数据预处理、模型搭建、训练评估和可视化分析。

## 项目结构
```
├── skill_test/                         # 技能测试核心文件
│   ├── 神经网络模型实现_房价预测.ipynb    # 完整Jupyter Notebook
│   ├── house_prices.csv                # 数据集
│   ├── house_prices_cols.txt           # 特征列说明
│   └── house_price_model.keras         # 训练好的模型
├── figures/                            # 可视化图表
│   ├── training_curve.png              # 训练曲线
│   ├── pred_vs_true.png                # 预测值vs真实值
│   ├── residuals.png                   # 残差图
│   └── label_distribution.png          # 标签分布
├── check_v2.py                         # 检查脚本
├── fill_v3.py                          # 数据填充脚本
├── read_report.py                      # 报告读取脚本
├── metrics.json                        # 评估指标
└── README.md                           # 项目说明
```

## 技术栈
- Python 3.13
- TensorFlow 2.21 / Keras
- scikit-learn 1.8
- Pandas / NumPy / Matplotlib

## 模型架构
全连接神经网络，包含：
- 输入层：数值化特征
- 多个隐藏层：Dense + Dropout（过拟合控制）
- 输出层：回归预测

## 实验内容
1. **数据预处理**：缺失值处理、特征编码、特征缩放
2. **模型搭建**：全连接网络结构设计
3. **模型训练**：损失函数、优化器配置
4. **过拟合控制**：Dropout、早停
5. **模型评估**：MSE、RMSE、R²等指标
6. **可视化分析**：训练曲线、预测对比、残差图

## 运行环境
```bash
pip install tensorflow pandas numpy scikit-learn matplotlib
```

## 使用方法
打开 `skill_test/神经网络模型实现_房价预测.ipynb`，按顺序执行所有单元格。

---
**作者**：liem
**框架**：TensorFlow 2.21
**数据集**：Kaggle House Prices
