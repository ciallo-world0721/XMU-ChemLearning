# Statistical Thermodynamics Exercises 中文翻译与详细解答

本文根据 `statthermo_exercise.pdf` 翻译整理，并尽量采用 `statthermo_formulae.pdf` 中的符号：

- 分子配分函数： $q = q_{trans} q_{rot} q_{vib} q_{elec}$
- 规范配分函数： $Q_N = q^N / N!$ （对不可分辨粒子，平动部分带 $N!$ ）
- 转动特征温度： $\theta_{rot} = B/k$
- 振动特征温度： $\theta_{vib} = h\nu_0/k$
- 玻尔兹曼因子： $exp(-\varepsilon/kT)$

文中 $k$ 为 Boltzmann 常数， $h$ 为 Planck 常数， $R = N_A k$ 。

---

## 1. 四个可分辨粒子的微观态数

**题目翻译**

考虑一组能级，其能量分别为 $0, 1, 2, 3, 4, 5, 6$ 单位。证明：对于 4 个**可分辨**粒子、总能量为 $6$ 单位的情形，微观态数 $\Omega = 84$ 。如果把能级间隔加倍，使能量改为 $0, 2, 4, 6$ ，新的 $\Omega$ 是多少？

**解答**

对 4 个可分辨粒子，微观态就是四元组

$$
(e_1, e_2, e_3, e_4)
$$

其中每个 $e_i$ 取允许能级，且满足

$$
e_1 + e_2 + e_3 + e_4 = 6.
$$

### 情形 1：能级为 $0,1,2,3,4,5,6$

因为总能量只有 6，所以这里只是在数**非负整数解**的个数：

$$
e_1 + e_2 + e_3 + e_4 = 6,\qquad e_i \ge 0.
$$

由插板法，

$$
\Omega = \binom{6+4-1}{4-1} = \binom{9}{3} = 84.
$$

因此

$$
\boxed{\Omega = 84}
$$

### 情形 2：能级为 $0,2,4,6$

令 $e_i = 2 n_i$ ，其中 $n_i = 0,1,2,3$ 。总能量条件变成

$$
2(n_1+n_2+n_3+n_4)=6
$$

即

$$
n_1+n_2+n_3+n_4=3.
$$

仍然数非负整数解：

$$
\Omega = \binom{3+4-1}{4-1} = \binom{6}{3} = 20.
$$

故新值为

$$
\boxed{\Omega = 20}
$$

---

## 2. 两个热块接触后的熵变与涨落概率

**题目翻译**

若某物体在定容下由 $T_i$ 升到 $T_f$ ，且热容为 $C_V$ ，则熵变

$$
\Delta S = C_V \ln(T_f/T_i).
$$

两个完全相同的热块，热容均为 $C_V$ ，一个初温为 $T+\delta T$ ，另一个初温为 $T-\delta T$ 。将它们接触并达到平衡：

1. 求平衡温度；
2. 证明整个系统熵变为
   $$
   \Delta S = C_V \ln\!\left(\frac{T^2}{(T+\delta T)(T-\delta T)}\right);
   $$
3. 并进一步写成
   $$
   \Delta S = -C_V \ln\!\left(1-\frac{\delta T^2}{T^2}\right);
   $$
4. 当 $\delta T$ 很小时，用 $ln(1+x)\approx x$ 证明
   $$
   \Delta S \approx C_V \left(\frac{\delta T}{T}\right)^2;
   $$
5. 当 $T=300 K$ ， $\delta T=0.1 K$ ， $C_V=25 J K^{-1}$ 时，求达到平衡后又自发回到初始温度分布的概率；
6. 哪个 $\delta T$ 会使该概率为 $0.001$ ？并评论结果。

**解答**

### 2.1 平衡温度

两块相同、热容相同，且系统与外界绝热。能量守恒给出

$$
C_V(T+\delta T) + C_V(T-\delta T) = 2 C_V T_{\rm eq}.
$$

所以

$$
\boxed{T_{\rm eq}=T.}
$$

### 2.2 总熵变

热块 1 从 $T+\delta T$ 变到 $T$ ：

$$
\Delta S_1 = C_V \ln\!\left(\frac{T}{T+\delta T}\right).
$$

热块 2 从 $T-\delta T$ 变到 $T$ ：

$$
\Delta S_2 = C_V \ln\!\left(\frac{T}{T-\delta T}\right).
$$

总熵变为

$$
\Delta S = \Delta S_1 + \Delta S_2
= C_V \ln\!\left(\frac{T}{T+\delta T}\right) + C_V \ln\!\left(\frac{T}{T-\delta T}\right).
$$

合并对数：

$$
\Delta S = C_V \ln\!\left(\frac{T^2}{(T+\delta T)(T-\delta T)}\right).
$$

又因为

$$
(T+\delta T)(T-\delta T)=T^2-\delta T^2=T^2\left(1-\frac{\delta T^2}{T^2}\right),
$$

所以

$$
\Delta S
= C_V \ln\!\left(\frac{1}{1-\delta T^2/T^2}\right)
= -C_V \ln\!\left(1-\frac{\delta T^2}{T^2}\right).
$$

即

$$
\boxed{\Delta S = -C_V \ln\!\left(1-\frac{\delta T^2}{T^2}\right).}
$$

### 2.3 小温差近似

令

$$
x=-\frac{\delta T^2}{T^2},
$$

当 $|x| << 1$ 时，

$$
\ln(1+x)\approx x.
$$

于是

$$
\Delta S \approx -C_V\left(-\frac{\delta T^2}{T^2}\right)
= C_V\left(\frac{\delta T}{T}\right)^2.
$$

故

$$
\boxed{\Delta S \approx C_V\left(\frac{\delta T}{T}\right)^2.}
$$

### 2.4 回到初始状态的概率

根据玻尔兹曼思想，熵降低 $\Delta S$ 的涨落概率尺度为

$$
P \sim \exp(-\Delta S/k).
$$

先算熵变：

$$
\Delta S \approx 25\left(\frac{0.1}{300}\right)^2
= 2.78\times 10^{-6}\ {\rm J\,K^{-1}}.
$$

因此

$$
\frac{\Delta S}{k}
 \approx \frac{2.78\times10^{-6}}{1.380649\times10^{-23}}
 \approx 2.01\times10^{17}.
$$

所以

$$
P \approx \exp(-2.01\times10^{17}).
$$

这几乎等于 0。若写成 10 为底的数量级，

$$
\log_{10} P \approx -8.74\times 10^{16}.
$$

即

$$
\boxed{P \approx \exp(-2.01\times10^{17}) \approx 0.}
$$

### 2.5 当概率为 $0.001$ 时的 $\delta T$

令

$$
\exp(-\Delta S/k)=10^{-3},
$$

则

$$
\Delta S = k\ln(1000).
$$

又用小温差式

$$
C_V\left(\frac{\delta T}{T}\right)^2 = k\ln(1000),
$$

所以

$$
\delta T
= T\sqrt{\frac{k\ln(1000)}{C_V}}.
$$

代入数值：

$$
\delta T
= 300\sqrt{\frac{(1.380649\times10^{-23})\ln 1000}{25}}
\approx 5.86\times 10^{-10}\ {\rm K}.
$$

故

$$
\boxed{\delta T \approx 5.9\times10^{-10}\ {\rm K}}
$$

### 2.6 评论

- 宏观物体的热涨落极其微小。
- $0.1 K$ 这样的温差对宏观系统来说已经巨大到几乎绝不可能自发恢复。
- 若要让“恢复初态”的概率达到 $10^{-3}$ ，温差必须小到 $10^{-10} K$ 量级，这说明宏观热力学不可逆性本质上来自微观态数的巨大不对称。

---

## 3. 系统 + 热浴模型中的概率分布

**题目翻译**

仍考虑第 1 题中四个粒子和能级，总能量为 $6$ 。把粒子 1 视为“系统”，其余 3 个粒子视为“热浴”。若系统能量为 $E_m=0$ ，证明系统加热浴可取的微观态数 $\Omega_m=28$ 。再对 $E_m=1,2,\dots,6$ 重复计算。

系统处于微观态 $m$ 的概率为

$$
P_m = \Omega_m/\Omega_{\rm tot},
$$

其中 $\Omega_{\mathrm{tot}}$ 为所有系统能量下微观态总数。说明为什么 $ln P_m$ 对 $E_m$ 作图应近似为直线；用你的数据作图（忽略 $E_m=5,6$ 两点）并评论。

**解答**

总能量固定为 6。当系统能量为 $E_m$ 时，热浴的能量为

$$
E_{\rm bath}=6-E_m.
$$

于是 $\Omega_m$ 就是三个粒子分配能量 $6-E_m$ 的方法数，即非负整数解个数：

$$
e_2+e_3+e_4 = 6-E_m.
$$

故

$$
\Omega_m = \binom{(6-E_m)+3-1}{3-1}
= \binom{8-E_m}{2}.
$$

逐项得到：

| $E_m$ | $\Omega_m$ |
|---|---:|
| 0 | 28 |
| 1 | 21 |
| 2 | 15 |
| 3 | 10 |
| 4 | 6 |
| 5 | 3 |
| 6 | 1 |

总微观态数

$$
\Omega_{\rm tot}=28+21+15+10+6+3+1=84,
$$

与第 1 题一致。

因此概率为

| $E_m$ | $P_m = \Omega_m/84$ | $ln P_m$ |
|---|---:|---:|
| 0 | 1/3 | -1.0986 |
| 1 | 1/4 | -1.3863 |
| 2 | 15/84 | -1.7228 |
| 3 | 10/84 | -2.1282 |
| 4 | 6/84 | -2.6391 |
| 5 | 3/84 | -3.3322 |
| 6 | 1/84 | -4.4308 |

### 为什么 $ln P_m$ 对 $E_m$ 应近似线性？

在正则系综中，

$$
P_m \propto \exp(-E_m/kT),
$$

因此

$$
\ln P_m = \text{const} - \frac{E_m}{kT},
$$

应为斜率为 $-1/kT$ 的直线。

本题中 $P_m$ 由热浴的态数 $\Omega_m$ 决定；当热浴足够大时，

$$
\Omega_m \propto \exp(-E_m/kT),
$$

所以 $ln P_m$ 近似线性。

### 评论

- 对 $E_m = 0$ 到 $4$ ，点大致落在一直线上。
- $E_m=5,6$ 偏离更明显，因为热浴只有 3 个粒子，并不够“大”，有限尺寸效应很明显。
- 这说明玻尔兹曼分布是“大热浴极限”下的结果；小热浴只会近似服从。

---

## 4. 两能级系统（无简并）

**题目翻译**

考虑 $N$ 个互不相互作用的不可分辨粒子，每个粒子只有两个能级： $0$ 和 $\Delta$ 。

1. 写出单粒子配分函数 $q$ ，并给出 $kT >> \Delta$ 与 $kT << \Delta$ 的极限；
2. 用 $q$ 推导内能 $U$ ；
3. 证明热容
   $$
   C_V = Nk\left(\frac{\Delta}{kT}\right)^2
   \frac{\exp(\Delta/kT)}{[\exp(\Delta/kT)+1]^2};
   $$
4. 求热容最大值对应的温度及其大小。

**解答**

### 4.1 单粒子配分函数

两能级分别为 $0$ 和 $\Delta$ ，所以

$$
q = 1 + \exp(-\Delta/kT).
$$

极限：

- 当 $kT << \Delta$ ， $exp(-\Delta/kT) \to 0$ ，所以
  $$
  q \to 1.
  $$
- 当 $kT >> \Delta$ ， $exp(-\Delta/kT) \to 1$ ，所以
  $$
  q \to 2.
  $$

即

$$
\boxed{q = 1+\exp(-\Delta/kT)}
$$

### 4.2 内能

由公式表，

$$
U = NkT^2\left(\frac{\partial \ln q}{\partial T}\right)_V.
$$

先求

$$
\ln q = \ln\!\left[1+\exp(-\Delta/kT)\right].
$$

对 $T$ 求导：

$$
\frac{\partial \ln q}{\partial T}
= \frac{1}{q}\exp(-\Delta/kT)\frac{\Delta}{kT^2}.
$$

故

$$
U = NkT^2 \cdot \frac{\Delta}{kT^2}\frac{\exp(-\Delta/kT)}{1+\exp(-\Delta/kT)}
$$

即

$$
\boxed{
U = \frac{N\Delta\,\exp(-\Delta/kT)}{1+\exp(-\Delta/kT)}
= \frac{N\Delta}{\exp(\Delta/kT)+1}
}
$$

极限：

- $kT << \Delta$ 时， $exp(\Delta/kT)$ 很大，所以
  $$
  U \to 0.
  $$
- $kT >> \Delta$ 时， $exp(\Delta/kT)\approx 1$ ，所以
  $$
  U \to \frac{N\Delta}{2}.
  $$

解释：

- 低温下几乎所有粒子都在基态，故内能趋近 0。
- 高温下两个能级几乎等概率占据，平均每粒子能量为 $\Delta/2$ 。

### 4.3 热容

由定义

$$
C_V = \left(\frac{\partial U}{\partial T}\right)_V.
$$

从

$$
U = \frac{N\Delta}{\exp(\Delta/kT)+1}
$$

出发，令 $x=\Delta/kT$ ，则

$$
U = \frac{N\Delta}{e^x+1},\qquad \frac{dx}{dT}=-\frac{\Delta}{kT^2}=-\frac{x}{T}.
$$

于是

$$
\frac{dU}{dT}
= N\Delta\left[-\frac{e^x}{(e^x+1)^2}\right]\frac{dx}{dT}
= N\Delta \frac{e^x}{(e^x+1)^2}\frac{x}{T}.
$$

再代入 $x=\Delta/kT$ 得

$$
\boxed{
C_V = Nk\left(\frac{\Delta}{kT}\right)^2
\frac{\exp(\Delta/kT)}{[\exp(\Delta/kT)+1]^2}
}
$$

#### 两端极限

- 当 $kT << \Delta$ ， $x>>1$ ，分母约为 $e^{2x}$ ，故
  $$
  C_V \sim Nk x^2 e^{-x}\to 0.
  $$
- 当 $kT >> \Delta$ ， $x<<1$ ，分式趋近 $1/4$ ，但前面的 $x^2 \to 0$ ，故
  $$
  C_V \to 0.
  $$

物理意义：

- 低温时几乎无人能被激发，吸热能力很弱。
- 高温时两个能级都已接近半满，再升温也很难进一步改变布居，因此热容再次趋零。

这是一条典型的 **Schottky 峰**。

### 4.4 热容最大值

令 $x=\Delta/kT$ ，则

$$
\frac{C_V}{Nk} = \frac{x^2 e^x}{(e^x+1)^2}.
$$

对 $x$ 求导并令零，可得极值条件

$$
e^x(x-2) + x + 2 = 0.
$$

数值解为

$$
x_{\max} \approx 2.399.
$$

因此

$$
\boxed{T_{\max} \approx \frac{\Delta}{2.399\,k} \approx 0.417\,\frac{\Delta}{k}}
$$

最大热容为

$$
\left(\frac{C_V}{Nk}\right)_{\max} \approx 0.439.
$$

即

$$
\boxed{C_{V,\max} \approx 0.439\,Nk.}
$$

---

## 5. 两能级系统（有简并）

**题目翻译**

与第 4 题相同，但低能级简并度为 $g_0$ ，高能级简并度为 $g_1$ 。

**解答**

### 5.1 配分函数

单粒子配分函数

$$
\boxed{q = g_0 + g_1 \exp(-\Delta/kT)}
$$

极限：

- $kT << \Delta$ ：
  $$
  q \to g_0.
  $$
- $kT >> \Delta$ ：
  $$
  q \to g_0 + g_1.
  $$

### 5.2 内能

由

$$
U = NkT^2\left(\frac{\partial \ln q}{\partial T}\right)_V
$$

得

$$
\boxed{
U = \frac{N\Delta\, g_1 \exp(-\Delta/kT)}{g_0 + g_1 \exp(-\Delta/kT)}
= \frac{N\Delta\, g_1}{g_0 \exp(\Delta/kT)+g_1}
}
$$

极限：

- $kT << \Delta$ ：
  $$
  U \to 0.
  $$
- $kT >> \Delta$ ：
  $$
  U \to N\Delta \frac{g_1}{g_0+g_1}.
  $$

解释：高温下所有**量子态**几乎等概率占据，因此高能级所占比例是 $g_1/(g_0+g_1)$ 。

### 5.3 热容

直接类比第 4 题可得

$$
\boxed{
C_V
= Nk\left(\frac{\Delta}{kT}\right)^2
\frac{g_0 g_1 \exp(-\Delta/kT)}{\left[g_0+g_1\exp(-\Delta/kT)\right]^2}
}
$$

也可写成

$$
C_V
= Nk\left(\frac{\Delta}{kT}\right)^2
\frac{g_0 g_1 \exp(\Delta/kT)}{\left[g_0\exp(\Delta/kT)+g_1\right]^2}.
$$

### 5.4 曲线与第 4 题相比如何变化？

- 仍然在低温与高温两端趋于 0。
- 仍然有 Schottky 型峰。
- 若 $g_1 > g_0$ ，高能级简并度更大，激发更“有利”，峰位会向较低温移动，峰形也会改变。
- 若 $g_0 > g_1$ ，则相反，峰位一般向较高温移动。
- 高温内能极限不再是 $N\Delta/2$ ，而是 $N\Delta g_1/(g_0+g_1)$ 。

---

## 6. 改变能量零点后熵表达式形式不变

**题目翻译**

证明：将能量零点平移，即把 $q$ 改写为

$$
q' = q \exp(-\varepsilon_0/kT),
$$

并不会改变教材第 4.3.2 节给出的熵表达式的形式。

**解答**

对转动、振动等内模，自由度熵常写成

$$
S = Nk\ln q + \frac{U}{T}.
$$

若能量整体平移 $\varepsilon_0$ ，则每个能级都变成

$$
\varepsilon_i' = \varepsilon_i + \varepsilon_0.
$$

所以

$$
q' = \sum_i \exp[-(\varepsilon_i+\varepsilon_0)/kT]
= e^{-\varepsilon_0/kT} q.
$$

于是

$$
\ln q' = \ln q - \frac{\varepsilon_0}{kT}.
$$

同时，内能整体增加 $N\varepsilon_0$ ：

$$
U' = U + N\varepsilon_0.
$$

代入熵表达式：

$$
S' = Nk\ln q' + \frac{U'}{T}
= Nk\left(\ln q - \frac{\varepsilon_0}{kT}\right) + \frac{U+N\varepsilon_0}{T}.
$$

展开后

$$
S' = Nk\ln q - \frac{N\varepsilon_0}{T} + \frac{U}{T} + \frac{N\varepsilon_0}{T}
= Nk\ln q + \frac{U}{T}
= S.
$$

所以熵的表达形式不变，且数值也不变：

$$
\boxed{S' = S.}
$$

---

## 7. 一维箱中粒子的平动配分函数； $N_2$ 的热波长与三维平动配分函数

**题目翻译**

1. 推导质量为 $m$ 的粒子限制在长度为 $a$ 的一维箱中的配分函数；
2. 计算 $N_2$ 在 $298 K$ 时的热波长 $\Lambda$ ；
3. 计算 $N_2$ 在 $298 K$ 、 $1 bar$ 下的摩尔体积，并据此求在该条件下 1 mol $N_2$ 的三维平动配分函数；评论其大小。

**解答**

### 7.1 一维箱中的配分函数

一维箱能级为

$$
E_n = \frac{n^2 h^2}{8ma^2},\qquad n=1,2,3,\dots
$$

因此

$$
q_{1{\rm D}} = \sum_{n=1}^{\infty} \exp\!\left(-\frac{n^2 h^2}{8ma^2 kT}\right).
$$

当能级间隔远小于 $kT$ 时，可把求和近似为积分：

$$
q_{1{\rm D}} \approx \int_0^\infty \exp(-\alpha n^2)\,dn,
\qquad
\alpha = \frac{h^2}{8ma^2kT}.
$$

用高斯积分

$$
\int_0^\infty e^{-\alpha n^2} dn = \frac{1}{2}\sqrt{\frac{\pi}{\alpha}},
$$

得

$$
q_{1{\rm D}}
\approx \frac{1}{2}\sqrt{\frac{8\pi ma^2kT}{h^2}}
= \frac{a}{h}\sqrt{2\pi mkT}.
$$

所以

$$
\boxed{q_{1{\rm D}} \approx \frac{a}{h}\sqrt{2\pi mkT}}
$$

该近似成立条件是：

- 箱子足够大；
- 温度不太低；
- 即相邻平动能级间隔远小于 $kT$ 。

### 7.2 $N_2$ 在 $298 K$ 时的热波长

由

$$
q_{\rm trans,3D} = \left(\frac{2\pi mkT}{h^2}\right)^{3/2}V = \frac{V}{\Lambda^3}
$$

定义热波长

$$
\Lambda = \frac{h}{\sqrt{2\pi mkT}}.
$$

对 $N_2$ ，单分子质量

$$
m = 28.0134\,u \approx 4.65\times10^{-26}\ {\rm kg}.
$$

代入 $T=298 K$ ：

$$
\boxed{\Lambda \approx 1.91\times10^{-11}\ {\rm m}}
$$

即约 $0.019 nm$ 。

### 7.3 摩尔体积与三维平动配分函数

理想气体摩尔体积：

$$
V_m = \frac{RT}{p}.
$$

取 $p=1.0\times10^5 Pa$ ，则

$$
V_m = \frac{(8.314)(298)}{10^5}
\approx 2.48\times10^{-2}\ {\rm m^3\,mol^{-1}}.
$$

故

$$
\boxed{V_m \approx 2.48\times10^{-2}\ {\rm m^3\,mol^{-1}}}
$$

对单个分子，处在该摩尔体积对应的平均体积 $V_m/N_A$ 中时，

$$
q_{\rm trans,3D}
= \left(\frac{2\pi mkT}{h^2}\right)^{3/2}\frac{V_m}{N_A}
\approx 5.90\times10^6.
$$

所以单分子平动配分函数非常大：

$$
\boxed{q_{\rm trans,3D} \approx 5.90\times10^6}
$$

若写成 1 mol 的规范配分函数，

$$
Q_N = \frac{q^N}{N!},
$$

则其值会大得惊人；通常讨论时更有意义的是 $\ln Q_N$ ，它也是一个极大的正数。

### 评论

- 平动能级极其密集，所以 $q_trans$ 非常大。
- 这也是为什么常温下气体平动自由度几乎总能视为经典连续极限。

---

## 8. 双原子分子的转动配分函数

**题目翻译**

1. 用刚性转子模型推导双原子分子的转动配分函数，并说明何为对称数；
2. 已知 $N_2$ 的转动常数 $\tilde B = 1.999 cm^{-1}$ ，求 $\theta_{rot}$ 与 $298 K$ 下的转动配分函数，并与第 7 题比较。

**解答**

### 8.1 一般推导

刚性转子能级：

$$
E_J = BJ(J+1),\qquad J=0,1,2,\dots
$$

每个 $J$ 的简并度为 $2J+1$ ，故

$$
q_{\rm rot} = \sum_{J=0}^\infty (2J+1)\exp[-BJ(J+1)/kT].
$$

若 $kT >> B$ ，能级稠密，可用积分近似：

$$
q_{\rm rot}
\approx \frac{1}{\sigma}\int_0^\infty (2J+1)\exp[-BJ(J+1)/kT]\,dJ
= \frac{kT}{\sigma B}.
$$

定义

$$
\theta_{\rm rot} = \frac{B}{k},
$$

则

$$
\boxed{q_{\rm rot} \approx \frac{T}{\sigma\theta_{\rm rot}}}
$$

对称数 $\sigma$ 的意义：

- 它用于避免把通过分子对称操作得到的不可区分转动状态重复计数。
- 异核双原子分子 $\sigma=1$ ；
- 同核双原子分子 $\sigma=2$ 。

### 8.2 $N_2$ 的数值

$N_2$ 为同核双原子分子，所以 $\sigma=2$ 。

由

$$
\theta_{\rm rot} = \frac{hc\tilde B}{k}
= (1.4387769\ {\rm K\,cm}) \times 1.999\ {\rm cm^{-1}}
\approx 2.88\ {\rm K}.
$$

故

$$
\boxed{\theta_{\rm rot} \approx 2.88\ {\rm K}}
$$

在 $298 K$ ，

$$
q_{\rm rot} \approx \frac{298}{2\times2.88} \approx 51.8.
$$

所以

$$
\boxed{q_{\rm rot}(298\ {\rm K}) \approx 51.8}
$$

### 评论

- $q_rot$ 显著大于 1，说明常温下许多转动态都被热激发。
- 但它仍远小于第 7 题中的 $q_trans \sim 10^6$ ，因为平动能级比转动能级更密。

---

## 9. 双原子分子的振动配分函数（谐振子）

**题目翻译**

1. 用谐振子模型，在能量从势阱底部算起时，写出振动配分函数求和式，证明它是几何级数，并写出无穷和；结果用 $\theta_vib$ 表示；
2. 已知 $N_2$ 的振动频率 $2360 cm^{-1}$ ，求 $\theta_vib$ 以及 $298 K$ 下的振动配分函数：
   - 以势阱底部为零点；
   - 以最低振动能级为零点；
   并评论结果。

**解答**

### 9.1 从势阱底部计能量

谐振子能级为

$$
E_v = \left(v+\frac12\right)h\nu_0,\qquad v=0,1,2,\dots
$$

于是

$$
q_{\rm vib}
= \sum_{v=0}^\infty \exp\!\left[-\frac{(v+1/2)h\nu_0}{kT}\right].
$$

写出前几项：

$$
q_{\rm vib}
= e^{-h\nu_0/2kT}
+ e^{-3h\nu_0/2kT}
+ e^{-5h\nu_0/2kT} + \cdots
$$

这是几何级数：

- 首项
  $$
  a = e^{-h\nu_0/2kT}
  $$
- 公比
  $$
  r = e^{-h\nu_0/kT}
  $$

所以

$$
q_{\rm vib} = \frac{a}{1-r}
= \frac{\exp(-h\nu_0/2kT)}{1-\exp(-h\nu_0/kT)}.
$$

令

$$
\theta_{\rm vib} = \frac{h\nu_0}{k},
$$

则

$$
\boxed{
q_{\rm vib}
= \frac{\exp(-\theta_{\rm vib}/2T)}{1-\exp(-\theta_{\rm vib}/T)}
}
$$

### 9.2 以最低振动能级为零点

若把零点能去掉，则能级变成

$$
E_v' = vh\nu_0,
$$

于是

$$
\boxed{
q_{\rm vib}' = \frac{1}{1-\exp(-\theta_{\rm vib}/T)}
}
$$

### 9.3 $N_2$ 的数值

由

$$
\theta_{\rm vib} = \frac{hc\tilde \nu}{k}
= (1.4387769\ {\rm K\,cm})\times 2360\ {\rm cm^{-1}}
\approx 3396\ {\rm K}.
$$

故

$$
\boxed{\theta_{\rm vib} \approx 3.40\times10^3\ {\rm K}}
$$

在 $298 K$ ，

$$
q_{\rm vib}
= \frac{\exp(-3395.5/596)}{1-\exp(-3395.5/298)}
\approx 0.00336
$$

所以从势阱底部计：

$$
\boxed{q_{\rm vib} \approx 3.36\times10^{-3}}
$$

而以最低振动态为零点时：

$$
q_{\rm vib}' = \frac{1}{1-\exp(-3395.5/298)}
\approx 1.000011.
$$

故

$$
\boxed{q_{\rm vib}' \approx 1.000011}
$$

### 评论

- 两者差别仅来自是否包含零点能因子 $exp(-\theta_vib/2T)$ 。
- 在热力学中，若只关心热激发，常采用基振动态为零点，此时 $q_vib'$ 更接近“热占据”的意义。
- $298 K$ 时 $\theta_vib >> T$ ，故振动几乎不被激发，配分函数非常接近 1。
- 与第 7、8 题相比，振动在室温下远不如平动和转动重要。

---

## 10. Morse 振子的振动配分函数

**题目翻译**

Morse 振子的能级写作

$$
\tilde E_v = v\tilde\omega - v(v+1)\tilde\omega x_e,
$$

其中最低能级 $v=0$ 的能量取为 0。写出用于求振动配分函数的前几项。对 $N_2$ （ $\tilde\omega=2360 cm^{-1}$ , $\tilde\omega x_e=14.5 cm^{-1}$ ）和 $Br_2$ （ $\tilde\omega=323 cm^{-1}$ , $\tilde\omega x_e=1.1 cm^{-1}$ ），在 $298 K$ 下求振动配分函数，并与忽略非谐性时的谐振子结果比较。

**解答**

### 10.1 一般表达式

因 $v=0$ 能量被取为 0，所以

$$
q_{\rm vib}
= \sum_{v=0}^\infty \exp\!\left(-\frac{hc\tilde E_v}{kT}\right)
= \sum_{v=0}^\infty \exp\!\left[-\frac{hc}{kT}\left(v\tilde\omega-v(v+1)\tilde\omega x_e\right)\right].
$$

前几项为

$$
q_{\rm vib}
= 1 + \exp\!\left[-\frac{hc(\tilde\omega-2\tilde\omega x_e)}{kT}\right] + \exp\!\left[-\frac{hc(2\tilde\omega-6\tilde\omega x_e)}{kT}\right] + \exp\!\left[-\frac{hc(3\tilde\omega-12\tilde\omega x_e)}{kT}\right] + \cdots
$$

### 10.2 $N_2$

$298 K$ 下逐项相加：

- $v=0$ ： $1$
- $v=1$ ： $1.295\times10^{-5}$
- $v=2$ ： $1.929\times10^{-10}$
- 更高项可忽略

因此

$$
\boxed{q_{\rm vib}^{\rm Morse}(N_2,298\,K) \approx 1.000013}
$$

若用简谐振子并以 $v=0$ 为零点：

$$
q_{\rm vib}^{\rm SHO} = \frac{1}{1-\exp(-\theta_{\rm vib}/T)}
\approx 1.000011.
$$

所以非谐性修正非常小：

$$
\boxed{q_{\rm vib}^{\rm SHO}(N_2,298\,K)\approx 1.000011}
$$

### 10.3 $Br_2$

逐项相加可得

$$
\boxed{q_{\rm vib}^{\rm Morse}(Br_2,298\,K) \approx 1.271}
$$

若用简谐近似：

$$
q_{\rm vib}^{\rm SHO}(Br_2,298\,K)\approx 1.266.
$$

即

$$
\boxed{q_{\rm vib}^{\rm SHO}(Br_2,298\,K)\approx 1.266}
$$

### 评论

- 对 $N_2$ ，振动量子太大，室温下几乎不激发，因此非谐性影响极小。
- 对 $Br_2$ ，振动频率较低，热激发更明显，Morse 修正稍大一些。
- 一般而言，非谐性会使高振动态间距缩小，从而略微增大配分函数。

---

## 11. 多原子分子的振动模

**题目翻译**

1. 若 $O_3$ 的构型分别为线型和折线型，各有多少个简正振动模？
2. $H_2O$ 的三个简正振动频率分别为 $3652, 1595, 3756 cm^{-1}$ 。从势阱底部计能量，求 $1000 K$ 下每个模的振动配分函数及总振动配分函数。

**解答**

### 11.1 $O_3$ 的振动模数

三原子分子有 $3N = 9$ 个自由度。

- 线型分子：振动模数 $= 3N-5 = 4$
- 非线型分子：振动模数 $= 3N-6 = 3$

故

$$
\boxed{\text{线型 } O_3: 4\text{ 个振动模}}
$$

$$
\boxed{\text{折线型 } O_3: 3\text{ 个振动模}}
$$

### 11.2 $H_2O$ 在 $1000 K$ 的振动配分函数

对每个模，

$$
q_{{\rm vib},i}
= \frac{\exp(-\theta_{{\rm vib},i}/2T)}{1-\exp(-\theta_{{\rm vib},i}/T)},
\qquad
\theta_{{\rm vib},i}= \frac{hc\tilde\nu_i}{k}.
$$

计算得到：

| 频率 $\tilde\nu_i / cm^{-1}$ | $\theta_vib / K$ | $q_vib$ at $1000 K$ |
|---:|---:|---:|
| 3652 | 5254.4 | 0.07266 |
| 1595 | 2294.8 | 0.35303 |
| 3756 | 5404.0 | 0.06737 |

总振动配分函数为各模乘积：

$$
q_{\rm vib,tot} = \prod_i q_{{\rm vib},i}.
$$

于是

$$
\boxed{q_{\rm vib,tot}(1000\,K)\approx 1.73\times10^{-3}}
$$

若不把零点能包含在内，则对应“去掉零点因子”的配分函数会大很多；这里题目明确要求从势阱底部计能量，因此结果小于 1 是正常的。

---

## 12. 电子配分函数

**题目翻译**

1. 对 Si(g) 的若干电子能级，写出各级简并度 $g_j$ 并求 $500 K$ 下的电子配分函数；
2. 室温下 $H_2$ 、 $O_2$ 、 $H_2^+$ 的电子配分函数各是多少？

**解答**

### 12.1 $Si(g)$ 在 $500 K$

给定能级：

| level | $^3P_0$ | $^3P_1$ | $^3P_2$ | $^1D_2$ | $^1S_0$ |
|---|---:|---:|---:|---:|---:|
| energy / $cm^{-1}$ | 0 | 76 | 222 | 6297 | 15390 |

原子项符号 $^{2S+1}L_J$ 的简并度是

$$
g_J = 2J+1.
$$

故

| level | $J$ | $g_J$ |
|---|---:|---:|
| $^3P_0$ | 0 | 1 |
| $^3P_1$ | 1 | 3 |
| $^3P_2$ | 2 | 5 |
| $^1D_2$ | 2 | 5 |
| $^1S_0$ | 0 | 1 |

电子配分函数为

$$
q_{\rm elec} = \sum_j g_j \exp(-\varepsilon_j/kT).
$$

若能量以波数给出，则

$$
\varepsilon_j/kT = \frac{hc\tilde\nu_j}{kT}.
$$

逐项计算（ $T=500 K$ ）：

- $^3P_0$ ： $1$
- $^3P_1$ ： $2.411$
- $^3P_2$ ： $2.640$
- $^1D_2$ ： $6.75\times10^{-8}$
- $^1S_0$ ：可忽略

所以

$$
\boxed{q_{\rm elec}({\rm Si},500\,K)\approx 6.050}
$$

### 12.2 室温下 $H_2$ 、 $O_2$ 、 $H_2^+$

室温时通常只有电子基态显著占据，因此电子配分函数近似为基态简并度：

- $H_2$ 基态为单重态：
  $$
  \boxed{q_{\rm elec}(H_2)\approx 1}
  $$
- $O_2$ 基态为 $^3\Sigma_g^-$ ，自旋多重度为 3：
  $$
  \boxed{q_{\rm elec}(O_2)\approx 3}
  $$
- $H_2^+$ 基态为双重态：
  $$
  \boxed{q_{\rm elec}(H_2^+)\approx 2}
  $$

---

## 13. $O_2$ 的电子配分函数

**题目翻译**

$O_2$ 的电子基态为 $^3\Sigma_g^-$ ；第一激发态为二重简并，并高于基态 $0.97 eV$ 。求 $298 K$ 和 $1000 K$ 下的电子配分函数（保留三位小数）。

**解答**

基态简并度取 3，第一激发态额外给出二重简并度 2，所以

$$
q_{\rm elec} = 3 + 2\exp(-\Delta E/kT),
\qquad \Delta E = 0.97\ {\rm eV}.
$$

取 $k = 8.61733\times10^{-5} eV K^{-1}$ 。

### $298 K$

$$
\frac{\Delta E}{kT}
= \frac{0.97}{(8.61733\times10^{-5})(298)}
\approx 37.8,
$$

故激发态贡献几乎为 0：

$$
q_{\rm elec}(298\,K)\approx 3.000.
$$

### $1000 K$

$$
\frac{\Delta E}{kT}
= \frac{0.97}{(8.61733\times10^{-5})(1000)}
\approx 11.26.
$$

于是

$$
2e^{-11.26} \approx 2.58\times10^{-5},
$$

所以

$$
q_{\rm elec}(1000\,K)\approx 3.0000258.
$$

保留三位小数：

$$
\boxed{q_{\rm elec}(298\,K)=3.000}
$$

$$
\boxed{q_{\rm elec}(1000\,K)=3.000}
$$

若保留更多位数，则 $1000 K$ 时约为 $3.000026$ 。

---

## 14. $N_2$ 在 $298 K$ 的摩尔定容热容

**题目翻译**

已知对 $N_2$ 有 $\tilde B = 1.999 cm^{-1}$ ， $\tilde\omega = 2360 cm^{-1}$ ，估计 $298 K$ 下的摩尔定容热容 $C_{V,m}$ 。

**解答**

判断各自由度是否“活跃”：

- 平动：一定活跃，贡献 $3/2 R$
- 转动： $\theta_{rot} \approx 2.88 K << 298 K$ ，充分活跃，双原子线型分子贡献 $R$
- 振动： $\theta_{vib} \approx 3396 K >> 298 K$ ，几乎冻结，贡献约为 0

所以

$$
C_{V,m} \approx \frac32 R + R = \frac52 R.
$$

数值为

$$
\boxed{C_{V,m}(N_2,298\,K)\approx \frac52 R \approx 20.8\ {\rm J\,mol^{-1}\,K^{-1}}}
$$

---

## 15. $H_2O(g)$ 在 $298 K$ 的摩尔定容热容；若线型会怎样

**题目翻译**

估计 $H_2O(g)$ 在 $298 K$ 的摩尔定容热容 $C_{V,m}$ 。若水分子假想为线型分子，这个值会怎样变化？

**解答**

真实水分子是**非线型三原子分子**。

### 实际的 $H_2O(g)$

- 平动贡献： $3/2 R$
- 非线型分子的转动贡献： $3/2 R$
- 室温下振动模大多未充分激发，可近似忽略

所以

$$
C_{V,m} \approx \frac32 R + \frac32 R = 3R.
$$

即

$$
\boxed{C_{V,m}(H_2O,g,298\,K)\approx 3R \approx 24.9\ {\rm J\,mol^{-1}\,K^{-1}}}
$$

### 若水分子假想为线型

线型分子只有 2 个转动自由度，因此转动贡献改为 $R$ 。于是

$$
C_{V,m} \approx \frac32 R + R = \frac52 R.
$$

即

$$
\boxed{C_{V,m}(\text{若线型})\approx \frac52 R \approx 20.8\ {\rm J\,mol^{-1}\,K^{-1}}}
$$

### 结论

若 $H_2O$ 假想为线型分子，其 $C_{V,m}$ 会比实际值少 $\frac12 R$ 。

---

## 16. 两能级系统与谐振子系统的 $q$ 、 $U$ 、 $C_V$ 的温度依赖比较

**题目翻译**

第 4 题讨论了只有两个能级的系统；而谐振子有无限多个等间隔能级。比较这两个系统中 $q$ 、 $U$ 、 $C_V$ 随温度的变化，并解释差异。

**解答**

### 两能级系统

- $q = 1 + e^{-\Delta/kT}$
  - 低温 $q \to 1$
  - 高温 $q \to 2$ ，有上限
- $U$
  - 低温 $U \to 0$
  - 高温 $U \to N\Delta/2$ ，饱和
- $C_V$
  - 低温 $\to 0$
  - 高温 $\to 0$
  - 中间出现一个 Schottky 峰

原因：只有一个激发能级，高温时上下能级都接近半满，继续升温不会显著增加能量。

### 谐振子系统

若以 $v=0$ 为零点，则

$$
q_{\rm vib} = \frac{1}{1-e^{-\theta_{\rm vib}/T}}.
$$

- 低温 $q \to 1$
- 高温时
  $$
  q \approx \frac{T}{\theta_{\rm vib}},
  $$
  会继续增大，没有有限上限

内能

$$
U = \frac{N h\nu_0}{e^{h\nu_0/kT}-1}.
$$

- 低温 $U \to 0$
- 高温 $U \to NkT$

热容

$$
C_V = Nk\left(\frac{\theta_{\rm vib}}{T}\right)^2
\frac{e^{\theta_{\rm vib}/T}}{(e^{\theta_{\rm vib}/T}-1)^2}.
$$

- 低温 $\to 0$
- 高温 $\to Nk$

### 根本差别

- 两能级系统的能量有上界，所以 $U$ 会饱和， $C_V$ 最终回落到 0。
- 谐振子有无限多激发态，没有饱和；高温下恢复经典极限， $U \propto T$ ， $C_V \to Nk$ 。

---

## 17. 三能级系统的 $U(T)$ 和 $C_V(T)$ 草图

**题目翻译**

考虑 $N$ 个粒子，每个粒子有三个无简并能级： $0$ 、 $\Delta_1$ 、 $\Delta_2$ ，并且 $\Delta_2 >> \Delta_1$ 。画出你预期的 $U$ 和 $C_V$ 随温度变化的示意图，并说明理由。

**解答**

### $U(T)$ 的形状

由于 $\Delta_2 >> \Delta_1$ ，升温过程会分成两个明显阶段：

1. 当 $kT \sim \Delta_1$ 时，粒子开始由基态跃迁到第一激发态， $U$ 首先从 0 增长到约 $N\Delta_1/2$ 附近。
2. 当 $kT \sim \Delta_2$ 时，第二激发态开始显著占据， $U$ 再次上升，最终在高温极限趋向三个能级等占据：
   $$
   U \to \frac{N(0+\Delta_1+\Delta_2)}{3}
   = \frac{N(\Delta_1+\Delta_2)}{3}.
   $$

因此 $U(T)$ 应呈现**两级台阶式上升**。

### $C_V(T)$ 的形状

每当某个能级间隔对应的热激发最明显时，都会出现一个 Schottky 型峰：

1. 在 $kT \sim \Delta_1$ 附近出现第一个峰；
2. 在 $kT \sim \Delta_2$ 附近出现第二个峰。

由于 $\Delta_2 >> \Delta_1$ ，这两个峰会相距很远，形成明显的**双峰结构**。

### 示意性描述

- $U(T)$ ：从 0 出发，先上升一段形成第一平台，再在更高温区继续上升到最终平台。
- $C_V(T)$ ：低温为 0，出现第一峰后回落，再在更高温区出现第二峰，最后再次趋于 0。

---

## 18. 谐振子的 $q_vib$ 、 $U$ 、 $C_V$

**题目翻译**

1. 对谐振子，在把 $v=0$ 状态作为能量零点时，推导 $q_vib$ ；
2. 进而求 $U$ 与 $C_V$ ；
3. 说明对该系统什么叫“低温”和“高温”，并求这两个极限下的 $U$ 与 $C_V$ ；
4. 评论这些极限值。

**解答**

### 18.1 振动配分函数

把 $v=0$ 作为零点后，能级为

$$
E_v = vh\nu_0,\qquad v=0,1,2,\dots
$$

因此

$$
q_{\rm vib} = \sum_{v=0}^\infty e^{-v h\nu_0/kT}.
$$

这是首项为 1、公比为 $e^{-h\nu_0/kT}$ 的几何级数，所以

$$
\boxed{
q_{\rm vib} = \frac{1}{1-\exp(-h\nu_0/kT)}
= \frac{1}{1-\exp(-\theta_{\rm vib}/T)}
}
$$

### 18.2 内能

由

$$
U = NkT^2\left(\frac{\partial \ln q_{\rm vib}}{\partial T}\right)_V
$$

得

$$
\boxed{
U = \frac{N h\nu_0}{\exp(h\nu_0/kT)-1}
= \frac{Nk\theta_{\rm vib}}{\exp(\theta_{\rm vib}/T)-1}
}
$$

### 18.3 热容

对 $U$ 再求导，可得

$$
\boxed{
C_V = Nk\left(\frac{\theta_{\rm vib}}{T}\right)^2
\frac{\exp(\theta_{\rm vib}/T)}{\left[\exp(\theta_{\rm vib}/T)-1\right]^2}
}
$$

### 18.4 低温与高温的含义

对振动系统：

- “低温”指 $T << \theta_{\rm vib}$ ，即 $kT << h\nu_0$
- “高温”指 $T >> \theta_{\rm vib}$ ，即 $kT >> h\nu_0$

### 18.5 低温极限

当 $T << \theta_{\rm vib}$ ， $e^{\theta_{\rm vib}/T}$ 极大：

$$
U \approx Nk\theta_{\rm vib} e^{-\theta_{\rm vib}/T} \to 0,
$$

$$
C_V \approx Nk\left(\frac{\theta_{\rm vib}}{T}\right)^2 e^{-\theta_{\rm vib}/T} \to 0.
$$

即

$$
\boxed{U \to 0,\qquad C_V \to 0 \quad (T \ll \theta_{\rm vib})}
$$

### 18.6 高温极限

当 $T >> \theta_{\rm vib}$ ，令 $x=\theta_{\rm vib}/T << 1$ ，则

$$
e^x - 1 \approx x.
$$

于是

$$
U \approx \frac{Nk\theta_{\rm vib}}{x} = NkT,
$$

$$
C_V \to Nk.
$$

故

$$
\boxed{U \to NkT,\qquad C_V \to Nk \quad (T \gg \theta_{\rm vib})}
$$

### 18.7 评论

- 低温下振动量子化明显，模几乎冻结，所以 $U$ 和 $C_V$ 都趋于 0。
- 高温下恢复经典等分配结果：每个谐振子贡献平均能量 $kT$ ，热容贡献 $k$ 。
- 这与两能级系统不同：谐振子没有能量上界，因此高温热容不会回落到 0，而是趋向常数 $Nk$ 。

---

## 19. $Br_2(g)$ 的振动内能与热容

**题目翻译**

光谱测量表明 $Br_2(g)$ 的振动频率为 $323 \ \mathrm{cm^{-1}}$ 。求其 $\theta_{\mathrm{vib}}$ ，并计算该分子在 $298 \ \mathrm{K}$ 时振动对摩尔内能与摩尔热容的贡献。并评论结果。

**解答**

振动特征温度为

$$
\theta_{\mathrm{vib}} = \frac{h c \tilde{\nu}}{k} = 1.4387769 \times 323 \approx 464.7 \ \mathrm{K}.
$$

因此

$$
\boxed{ \theta_{\mathrm{vib}} \approx 465 \ \mathrm{K} }.
$$

把 $v = 0$ 取为零能级时，

$$
U_{\mathrm{vib},m} = R \frac{\theta_{\mathrm{vib}}}{\exp(\theta_{\mathrm{vib}}/T)-1},
$$

$$
C_{V,\mathrm{vib},m} = R \left( \frac{\theta_{\mathrm{vib}}}{T} \right)^2
\frac{\exp(\theta_{\mathrm{vib}}/T)}{\left[ \exp(\theta_{\mathrm{vib}}/T)-1 \right]^2}.
$$

代入 $T = 298 \ \mathrm{K}$ 得

$$
U_{\mathrm{vib},m} \approx 1.03 \times 10^3 \ \mathrm{J \ mol^{-1}},
$$

$$
C_{V,\mathrm{vib},m} \approx 6.82 \ \mathrm{J \ mol^{-1} \ K^{-1}}.
$$

所以

$$
\boxed{ U_{\mathrm{vib},m}(298 \ \mathrm{K}) \approx 1.03 \ \mathrm{kJ \ mol^{-1}} }
$$

$$
\boxed{ C_{V,\mathrm{vib},m}(298 \ \mathrm{K}) \approx 6.82 \ \mathrm{J \ mol^{-1} \ K^{-1}} }.
$$

**评论**

- 对 $Br_2$ 而言， $\theta_{\mathrm{vib}}$ 已不算很高，因此室温下振动并非完全冻结。
- 与 $N_2$ 相比， $Br_2$ 的振动热容贡献明显更大。

---

## 20. $NO$ 的电子内能贡献

**题目翻译**

$NO$ 的电子基态是二重简并，在其上方 $121.1 \ \mathrm{cm^{-1}}$ 处还有一个二重简并激发态。求 $1000 \ \mathrm{K}$ 时电子部分对摩尔内能的贡献，并把它表示为平动与转动总贡献的百分比。电子热容随温度将如何变化？

**解答**

电子配分函数为

$$
q_{\mathrm{elec}} = 2 + 2 \exp \left( - \frac{\Delta \varepsilon}{kT} \right),
$$

其中

$$
\frac{\Delta \varepsilon}{k} = 1.4387769 \times 121.1 \approx 174.24 \ \mathrm{K}.
$$

于是

$$
U_{\mathrm{elec},m} = R \frac{ 2 (\Delta \varepsilon / k) \exp(-\Delta \varepsilon / kT) }
{ 2 + 2 \exp(-\Delta \varepsilon / kT) }.
$$

在 $T = 1000 \ \mathrm{K}$ 时，

$$
q_{\mathrm{elec}} \approx 3.680,
$$

$$
U_{\mathrm{elec},m} \approx 661 \ \mathrm{J \ mol^{-1}}.
$$

对线型双原子分子，平动加转动的摩尔内能为

$$
U_{\mathrm{trans+rot},m} = \frac{5}{2} RT \approx 20.8 \ \mathrm{kJ \ mol^{-1}}.
$$

故电子贡献所占百分比约为

$$
\frac{661}{(5/2)RT} \times 100\% \approx 3.18\%.
$$

因此

$$
\boxed{ U_{\mathrm{elec},m}(1000 \ \mathrm{K}) \approx 0.661 \ \mathrm{kJ \ mol^{-1}} }
$$

$$
\boxed{ \text{约占平动 + 转动总贡献的 } 3.2\% }.
$$

**热容随温度的变化**

- 低温下激发态几乎不占据， $C_{V,\mathrm{elec}} \to 0$ 。
- 当 $kT \sim \Delta \varepsilon$ 时出现 Schottky 峰。
- 高温下两个电子能级都近似等占据， $C_{V,\mathrm{elec}}$ 再次趋于 0。

---

## 21. $H^{35}Cl$ 的转动常数、配分函数与转动内能

**题目翻译**

已知 $H^{35}Cl$ 的键长为 $127.5 \ \mathrm{pm}$ 。

1. 计算 $\tilde{B}$ 和 $\theta_{\mathrm{rot}}$ ；
2. 求 $298 \ \mathrm{K}$ 时的转动配分函数和转动摩尔内能；
3. 求 $30 \ \mathrm{K}$ 时的转动配分函数；
4. 求 $30 \ \mathrm{K}$ 时的 $d q_{\mathrm{rot}} / dT$ ；
5. 进而求 $30 \ \mathrm{K}$ 时的转动摩尔内能。

**解答**

约化质量为

$$
\mu = \frac{m_{\mathrm{H}} m_{\mathrm{Cl}}}{m_{\mathrm{H}} + m_{\mathrm{Cl}}},
$$

转动惯量

$$
I = \mu R^2.
$$

代入 $R = 127.5 \ \mathrm{pm}$ 得

$$
I \approx 2.64 \times 10^{-47} \ \mathrm{kg \ m^2}.
$$

转动常数

$$
\tilde{B} = \frac{h}{8 \pi^2 c I} \approx 10.586 \ \mathrm{cm^{-1}},
$$

因此

$$
\theta_{\mathrm{rot}} = \frac{h c \tilde{B}}{k} \approx 15.23 \ \mathrm{K}.
$$

即

$$
\boxed{ \tilde{B} \approx 10.59 \ \mathrm{cm^{-1}} }, \qquad
\boxed{ \theta_{\mathrm{rot}} \approx 15.23 \ \mathrm{K} }.
$$

### 21.1 $298 \ \mathrm{K}$

异核双原子分子 $\sigma = 1$ ，高温近似下

$$
q_{\mathrm{rot}} \approx \frac{T}{\theta_{\mathrm{rot}}} \approx \frac{298}{15.23} \approx 19.6.
$$

逐项求和更准确可得

$$
q_{\mathrm{rot}}(298 \ \mathrm{K}) \approx 19.90.
$$

转动摩尔内能由

$$
U_{\mathrm{rot},m} = R T^2 \frac{1}{q_{\mathrm{rot}}} \frac{d q_{\mathrm{rot}}}{dT}
$$

给出，数值得

$$
U_{\mathrm{rot},m}(298 \ \mathrm{K}) \approx 2.44 \ \mathrm{kJ \ mol^{-1}} \approx RT.
$$

### 21.2 $30 \ \mathrm{K}$

此时不能使用高温近似，而应直接求和

$$
q_{\mathrm{rot}} = \sum_{J=0}^{\infty} (2J+1) \exp \left[ - \frac{\theta_{\mathrm{rot}} J(J+1)}{T} \right].
$$

逐项相加得

$$
\boxed{ q_{\mathrm{rot}}(30 \ \mathrm{K}) \approx 2.341 }.
$$

对温度求导：

$$
\frac{d q_{\mathrm{rot}}}{dT}
= \sum_{J=0}^{\infty} (2J+1)
\exp \left[ - \frac{\theta_{\mathrm{rot}} J(J+1)}{T} \right]
\frac{\theta_{\mathrm{rot}} J(J+1)}{T^2}.
$$

在 $30 \ \mathrm{K}$ 时

$$
\boxed{ \left. \frac{d q_{\mathrm{rot}}}{dT} \right|_{30 \ \mathrm{K}} \approx 0.0643 \ \mathrm{K^{-1}} }.
$$

于是

$$
U_{\mathrm{rot},m}(30 \ \mathrm{K}) = R T^2 \frac{1}{q_{\mathrm{rot}}} \frac{d q_{\mathrm{rot}}}{dT}
\approx 205 \ \mathrm{J \ mol^{-1}}.
$$

即

$$
\boxed{ U_{\mathrm{rot},m}(30 \ \mathrm{K}) \approx 0.205 \ \mathrm{kJ \ mol^{-1}} }.
$$

---

## 22. Einstein 固体模型

**题目翻译**

设固体中每个粒子都在平衡位置附近做三维简谐振动，且所有粒子的振动频率都相同，为 $\nu_E$ 。若有 $N$ 个粒子，证明内能和热容分别为

$$
U = \frac{3 N k \theta_E}{\exp(\theta_E/T)-1},
$$

$$
C_V = 3 N_A k \left( \frac{\theta_E}{T} \right)^2
\frac{\exp(\theta_E/T)}{[\exp(\theta_E/T)-1]^2},
$$

并求高温极限。与 Dulong-Petit 定律比较。

**解答**

每个粒子有 3 个彼此独立的一维简谐振子，因此总振动配分函数可看作单个一维振子的三倍自由度乘积。对一个一维简谐振子，若 $v = 0$ 取零能级，则

$$
q_{\mathrm{vib}} = \frac{1}{1-\exp(-\theta_E/T)}.
$$

故每个粒子的 3 维贡献给出

$$
U = 3 N k \frac{\theta_E}{\exp(\theta_E/T)-1}.
$$

对 $T$ 求导即得

$$
C_V = 3 N_A k \left( \frac{\theta_E}{T} \right)^2
\frac{\exp(\theta_E/T)}{[\exp(\theta_E/T)-1]^2}.
$$

当 $T \gg \theta_E$ 时，令 $x = \theta_E/T \ll 1$ ，则

$$
e^x - 1 \approx x.
$$

于是

$$
U \to 3 N k T,
$$

$$
C_V \to 3 N_A k = 3R.
$$

所以

$$
\boxed{ C_{V,m} \to 3R \quad (T \gg \theta_E) }.
$$

这正是 Dulong-Petit 定律。Einstein 模型在高温下正确，但在低温下预测的是指数衰减，而实验更接近 Debye 的 $T^3$ 定律。

---

## 23. $O_2(g)$ 在 $298 \ \mathrm{K}$ 的标准摩尔熵

**题目翻译**

对 $O_2$ ，已知 $\theta_{\mathrm{rot}} = 2.07 \ \mathrm{K}$ ， $\theta_{\mathrm{vib}} = 2256 \ \mathrm{K}$ 。计算 $298 \ \mathrm{K}$ 时的标准摩尔熵。需要考虑平动、转动和电子贡献；并说明为什么振动贡献可以忽略。

**解答**

标准态取 $p^\circ = 1 \ \mathrm{bar}$ 。平动熵可写为

$$
S_{\mathrm{trans},m} = R \left( \ln q_{\mathrm{trans}} + \frac{5}{2} \right),
$$

其中 $q_{\mathrm{trans}}$ 取标准摩尔体积对应的单分子配分函数。计算得

$$
S_{\mathrm{trans},m} \approx 152.1 \ \mathrm{J \ mol^{-1} \ K^{-1}}.
$$

转动部分对于同核双原子分子有

$$
q_{\mathrm{rot}} \approx \frac{T}{2 \theta_{\mathrm{rot}}}
= \frac{298}{2 \times 2.07} \approx 72.0,
$$

故

$$
S_{\mathrm{rot},m} = R ( \ln q_{\mathrm{rot}} + 1 )
\approx 43.9 \ \mathrm{J \ mol^{-1} \ K^{-1}}.
$$

$O_2$ 基态为三重态，电子熵贡献为

$$
S_{\mathrm{elec},m} = R \ln 3 \approx 9.13 \ \mathrm{J \ mol^{-1} \ K^{-1}}.
$$

故总熵

$$
S_m^\circ \approx 152.1 + 43.9 + 9.13 = 205.1 \ \mathrm{J \ mol^{-1} \ K^{-1}}.
$$

因此

$$
\boxed{ S_m^\circ ( O_2, 298 \ \mathrm{K} ) \approx 205 \ \mathrm{J \ mol^{-1} \ K^{-1}} }.
$$

**为什么振动可忽略**

因为

$$
\theta_{\mathrm{vib}} = 2256 \ \mathrm{K} \gg 298 \ \mathrm{K},
$$

振动激发几乎冻结， $q_{\mathrm{vib}} \approx 1$ ，故对熵的贡献很小。

---

## 24. 由质量标度估算熵

**题目翻译**

1. 已知 $He(g)$ 在 $298 \ \mathrm{K}$ 的标准摩尔熵为 $126.1 \ \mathrm{J \ mol^{-1} \ K^{-1}}$ ，且稀有气体熵可视为纯平动熵。利用 $q_{\mathrm{trans}} \propto m^{3/2}$ 估算 $Ar(g)$ 在同温度下的标准摩尔熵。
2. 用同样方法求 $N_2(g)$ 在 $298 \ \mathrm{K}$ 的平动熵贡献。
3. 已知 $N_2(g)$ 的标准摩尔熵为 $191.6 \ \mathrm{J \ mol^{-1} \ K^{-1}}$ ，估算其键长。

**解答**

由

$$
S_{\mathrm{trans},m} = R \left( \ln q_{\mathrm{trans}} + \frac{5}{2} \right)
$$

知质量改变引起的熵差为

$$
\Delta S_{\mathrm{trans},m} = \frac{3}{2} R \ln \left( \frac{m_2}{m_1} \right).
$$

### 24.1 $Ar$

$$
S_m^\circ ( Ar ) \approx 126.1 + \frac{3}{2} R \ln \left( \frac{39.95}{4.00} \right)
\approx 154.8 \ \mathrm{J \ mol^{-1} \ K^{-1}}.
$$

### 24.2 $N_2$ 的平动熵

$$
S_{\mathrm{trans},m} ( N_2 ) \approx 126.1 + \frac{3}{2} R \ln \left( \frac{28.01}{4.00} \right)
\approx 150.4 \ \mathrm{J \ mol^{-1} \ K^{-1}}.
$$

### 24.3 由剩余熵估算键长

转动熵约为

$$
S_{\mathrm{rot},m} \approx 191.6 - 150.4 = 41.2 \ \mathrm{J \ mol^{-1} \ K^{-1}}.
$$

对同核双原子分子，

$$
S_{\mathrm{rot},m} = R ( \ln q_{\mathrm{rot}} + 1 ),
\qquad
q_{\mathrm{rot}} \approx \frac{T}{2 \theta_{\mathrm{rot}}}.
$$

由此反解得

$$
\theta_{\mathrm{rot}} \approx 2.84 \ \mathrm{K},
\qquad
\tilde{B} \approx 1.98 \ \mathrm{cm^{-1}}.
$$

再由

$$
\tilde{B} = \frac{h}{8 \pi^2 c I},
\qquad
I = \mu R^2
$$

得到

$$
R \approx 110 \ \mathrm{pm}.
$$

因此

$$
\boxed{ R( N_2 ) \approx 1.10 \times 10^{-10} \ \mathrm{m} }.
$$

这个估算值与真实键长 $\sim 110 \ \mathrm{pm}$ 很接近。

---

## 25. 剩余熵与对称数

**题目翻译**

1. 解释为什么对 $CO$ ，计算熵与量热熵不一致，而对 $OCS$ 却一致。
2. 对 $CH_3D$ ，发现计算熵比热化学值大 $11.5 \ \mathrm{J \ mol^{-1} \ K^{-1}}$ 。解释原因，并说明剩余熵的来源。

**解答**

### 25.1 $CO$ 与 $OCS$

- 若简单把 $CO$ 当作异核双原子分子处理，通常认为转动对称数 $\sigma = 1$ 。
- 但从分子取向的统计可辨识性出发，实验上并不是所有“头尾互换”的定向都能完全独立保留下来，实际熵与简单统计模型会出现差异。
- 对 $OCS$ 这类明显非对称的线型三原子分子，头尾交换不会导致混淆，因此理论计数与实验熵更容易一致。

更简洁地说： $CO$ 的问题来自“几何上异核，但热力学上定向可区分性的处理较微妙”；而 $OCS$ 不存在这个模糊性。

### 25.2 $CH_3D$ 的剩余熵

$CH_3D$ 具有多个等价的取向或核自旋排列，其低温下不能完全通过单一有序排列消除。若理论计算按“所有微观取向完全可取且彼此独立”计数，就会比热化学第三定律熵大出一项剩余熵。

给出的差值

$$
11.5 \ \mathrm{J \ mol^{-1} \ K^{-1}}
$$

非常接近

$$
R \ln 4 = 11.53 \ \mathrm{J \ mol^{-1} \ K^{-1}}.
$$

因此可解释为存在 4 个等价取向所导致的剩余熵：

$$
\boxed{ S_{\mathrm{res}} \approx R \ln 4 }.
$$

---

## 26. 同核双原子分子的核自旋对称态数

**题目翻译**

对由核自旋为 $I$ 的原子形成的同核双原子分子，证明对称与反对称核自旋态数分别为讲义中给出的结果。

**解答**

总核自旋态数为

$$
(2I+1)^2.
$$

其中两核具有相同 $m_I$ 的态共有

$$
2I+1
$$

个，这些态在交换两核后不变，因此必为对称态。

其余态数为

$$
(2I+1)^2 - (2I+1) = (2I+1)(2I).
$$

这些态都以成对方式出现：例如 $|m_1, m_2 \rangle$ 与 $|m_2, m_1 \rangle$ 。每一对可以线性组合成一个对称态和一个反对称态，因此这部分均分为两类：

$$
\frac{ (2I+1)(2I) }{2} = I(2I+1).
$$

于是

$$
N_{\mathrm{antisym}} = I(2I+1),
$$

$$
N_{\mathrm{sym}} = (2I+1) + I(2I+1) = (I+1)(2I+1).
$$

所以

$$
\boxed{ N_{\mathrm{sym}} = (I+1)(2I+1) }, \qquad
\boxed{ N_{\mathrm{antisym}} = I(2I+1) }.
$$

---

## 27. 转动 Raman 光谱中的核自旋统计

**题目翻译**

1. 说明 $^{37}Cl_2(g)$ 的转动 Raman 光谱强度分布，并与 $^{37}Cl^{35}Cl$ 比较。
2. 比较 $H_2^-$ 与 $H_2$ 的转动 Raman 光谱。

**解答**

### 27.1 $^{37}Cl_2$ 与 $^{37}Cl^{35}Cl$

$^{35}Cl$ 与 $^{37}Cl$ 的核自旋均为 $I = 3/2$ ，为费米子。对 $^{37}Cl_2$ ：

- 核自旋对称态数为
  $$
  (I+1)(2I+1) = 10
  $$
- 反对称态数为
  $$
  I(2I+1) = 6
  $$

又因电子基态为 ${}^1 \Sigma_g^+$ ，电子与振动基态都是对称的，因此总波函数在交换两核时必须反对称。于是：

- 偶 $J$ 与奇 $J$ 的转动态会分别对应不同的核自旋权重；
- 光谱线会呈现奇偶 $J$ 交替强弱的图样，强度比约为 $10:6 = 5:3$ 。

对异核分子 $^{37}Cl^{35}Cl$ ，不存在交换完全相同核的问题，因此没有奇偶 $J$ 的核自旋统计限制，所有允许的 Raman 线都会出现，强度分布更平滑。

### 27.2 $H_2^-$ 与 $H_2$

相同点：

- 都是同核双原子体系；
- 都会受到核自旋统计的影响。

不同点：

- 若电子态对称性发生变化，则“偶 $J$ 对应 ortho 还是 para”的归属会反过来；
- 因而光谱中奇偶 $J$ 的相对强弱模式可能与 $H_2$ 对调。

核心结论是：核自旋统计决定了奇偶 $J$ 的布居权重，而电子波函数的交换对称性决定哪一组 $J$ 搭配哪一类核自旋态。

---

## 28. $O_2$ 与 ${}^{16}O{}^{18}O$ 的转动 Raman 光谱

**题目翻译**

已知 ${}^{16}O_2$ 与 ${}^{16}O{}^{18}O$ 的转动 Raman 线位移，解释谱图外观，求各自的转动常数并据此求 $O_2$ 的键长。

**解答**

转动 Raman 选择定则为

$$
\Delta J = \pm 2.
$$

线位移为

$$
\Delta \tilde{\nu} = \tilde{B} \left[ (J+2)(J+3) - J(J+1) \right]
= 4 \tilde{B} \left( J + \frac{3}{2} \right).
$$

### 28.1 ${}^{16}O_2$

${}^{16}O$ 的核自旋为 0，且 $O_2$ 电子基态的对称性使得只允许某一奇偶性的 $J$ 出现，因此相邻可见谱线对应的 $J$ 相差 2，故相邻线距为

$$
8 \tilde{B}.
$$

由实验线距

$$
26.010 - 14.450 = 11.560 \ \mathrm{cm^{-1}}
$$

得

$$
\tilde{B} = \frac{11.560}{8} \approx 1.445 \ \mathrm{cm^{-1}}.
$$

### 28.2 ${}^{16}O{}^{18}O$

异核分子不受同核核自旋统计限制，可见相邻转动 Raman 线对应相邻 $J$ ，故相邻线距为

$$
4 \tilde{B}.
$$

由线距

$$
13.650 - 8.190 = 5.460 \ \mathrm{cm^{-1}}
$$

得

$$
\tilde{B} = \frac{5.460}{4} \approx 1.365 \ \mathrm{cm^{-1}}.
$$

### 28.3 一致性与键长

由

$$
\tilde{B} = \frac{h}{8 \pi^2 c I}, \qquad I = \mu R^2
$$

求得

$$
R( {}^{16}O_2 ) \approx 120.78 \ \mathrm{pm},
$$

$$
R( {}^{16}O{}^{18}O ) \approx 120.76 \ \mathrm{pm}.
$$

两者一致，故

$$
\boxed{ R( O_2 ) \approx 121 \ \mathrm{pm} }.
$$

---

## 29. 偶数 $J$ 求和的高温极限

**题目翻译**

证明在 $kT \gg B$ 的极限下

$$
\sum_{\text{even } J} (2J+1) \exp \left[ - \frac{B J(J+1)}{kT} \right]
= \frac{kT}{2B}.
$$

**解答**

令 $J = 2K$ ，则求和式变为

$$
\sum_{K=0}^{\infty} (4K+1) \exp \left[ - \frac{B (2K)(2K+1)}{kT} \right].
$$

在高温极限下，可用积分近似。由于偶数 $J$ 只占全部 $J$ 的一半，而完整转动配分函数在高温下为

$$
\sum_{J=0}^{\infty} (2J+1) \exp \left[ - \frac{B J(J+1)}{kT} \right]
\approx \frac{kT}{B},
$$

因此偶数 $J$ 部分自然占其一半：

$$
\boxed{
\sum_{\text{even } J} (2J+1) \exp \left[ - \frac{B J(J+1)}{kT} \right]
\approx \frac{kT}{2B}
}.
$$

---

## 30. $Cl_2 \rightleftharpoons 2Cl$ 在 $1200 \ \mathrm{K}$ 的 $K_c$

**题目翻译**

利用给定的 $\theta_{\mathrm{vib}}$ 、 $\theta_{\mathrm{rot}}$ 、 $D_e$ 和电子态信息，求平衡

$$
Cl_2 \rightleftharpoons 2Cl
$$

在 $1200 \ \mathrm{K}$ 时的 $K_c$ 。

**解答思路**

使用讲义中的气相平衡常数表达式

$$
K_c = \frac{ f_{Cl}^2 }{ f_{Cl_2} } \frac{1}{c^\circ}
\exp \left( - \frac{\Delta \varepsilon_0}{kT} \right).
$$

其中：

- 原子 $Cl$ 的电子简并度来自 ${}^2 P_{3/2}$ ，故基态权重为 4；
- $Cl_2$ 为闭壳层，电子权重约为 1；
- 转动与振动仅对 $Cl_2$ 出现；
- $\Delta \varepsilon_0$ 要由原子能量零点与分子势阱底之间的差换算得到，注意使用 $D_e$ 而非 $D_0$ 。

计算时最容易出错的地方有两个：

1. $D_e = 20280 \ \mathrm{cm^{-1}}$ 必须先换算成每分子能量；
2. $K_c$ 与 $K_p$ 、以及标准态体积项之间不要混淆。

**逐步代入**

对标准态单分子平动配分函数，

$$
q_{\mathrm{trans}}^\circ
= \left( \frac{ 2 \pi m k T }{ h^2 } \right)^{3/2} \frac{V_m^\circ}{N_A},
\qquad
V_m^\circ = \frac{RT}{p^\circ}.
$$

在 $T = 1200 \ \mathrm{K}$ 时，

$$
q_{\mathrm{trans}}^\circ(Cl) \approx 2.68 \times 10^8,
$$

$$
q_{\mathrm{trans}}^\circ(Cl_2) \approx 7.58 \times 10^8.
$$

原子 $Cl$ 的电子基态为 ${}^2 P_{3/2}$ ，电子权重取 4，因此

$$
q^\circ(Cl) \approx 4 q_{\mathrm{trans}}^\circ(Cl).
$$

对分子 $Cl_2$ ：

$$
q_{\mathrm{rot}} \approx \frac{T}{2 \theta_{\mathrm{rot}}}
= \frac{1200}{2 \times 0.351}
\approx 1.709 \times 10^3.
$$

振动部分采用“从势阱底部计能量”的形式：

$$
q_{\mathrm{vib}}
= \frac{ \exp(-\theta_{\mathrm{vib}}/2T) }{ 1-\exp(-\theta_{\mathrm{vib}}/T) }
= \frac{ \exp(-808/2400) }{ 1-\exp(-808/1200) }
\approx 1.457.
$$

故

$$
q^\circ(Cl_2) \approx q_{\mathrm{trans}}^\circ(Cl_2) \, q_{\mathrm{rot}} \, q_{\mathrm{vib}}.
$$

解离能换成温度形式：

$$
\frac{D_e}{k}
= 1.4387769 \times 20280
\approx 2.918 \times 10^4 \ \mathrm{K}.
$$

因此

$$
\exp(-D_e/kT)
= \exp(-29178/1200)
\approx 2.75 \times 10^{-11}.
$$

代入平衡常数表达式得到

$$
K_c
= \frac{ f_{Cl}^2 }{ f_{Cl_2} } \frac{1}{c^\circ}
\exp(-D_e/kT)
\approx 1.68 \times 10^{-7}.
$$

所以

$$
\boxed{ K_c(1200 \ \mathrm{K}) \approx 1.7 \times 10^{-7} }.
$$

**评论**

- 尽管解离会显著增加平动状态数，但 $D_e$ 的指数抑制仍很强；
- 因而在 $1200 \ \mathrm{K}$ 时， $Cl_2$ 仍明显占优，解离并不充分。

---

## 31. $Na_2 \rightleftharpoons 2Na$

**题目翻译**

1. 由 $Na_2$ 的键长求转动惯量、转动常数与转动特征温度；
2. 已知振动频率和解离能，求 $1000 \ \mathrm{K}$ 时平衡
   $$
   Na_2 \rightleftharpoons 2Na
   $$
   的 $K_p$ 。

**解答**

### 31.1 转动惯量、转动常数与转动特征温度

已知键长 $R$（题给 $R=307.8\ \mathrm{pm}$）。对同核双原子分子 $Na_2$：

$$
\mu=\frac{m_{\mathrm{Na}}}{2},\qquad
I=\mu R^2=\frac{m_{\mathrm{Na}}}{2}R^2.
$$

转动常数（波数单位）为

$$
\tilde B=\frac{h}{8\pi^2 c I}.
$$

转动特征温度为

$$
\theta_{\mathrm{rot}}=\frac{hc\tilde B}{k}.
$$

代入题给参数后：

$$
\tilde B \approx 0.155\ \mathrm{cm^{-1}},\qquad
\theta_{\mathrm{rot}}\approx 0.223\ \mathrm{K}.
$$

### 31.2 振动特征温度

由题给振动波数 $\tilde\nu$（$159.2\ \mathrm{cm^{-1}}$）：

$$
\theta_{\mathrm{vib}}=\frac{hc\tilde\nu}{k}.
$$

代入得

$$
\theta_{\mathrm{vib}}\approx 229.1\ \mathrm{K}.
$$

### 31.3 平衡常数 $K_p$ 的符号表达

对反应

$$
Na_2 \rightleftharpoons 2Na,
$$

写成统计热力学形式：

$$
K_p
= \frac{\left(q^\circ_{Na}\right)^2}{q^\circ_{Na_2}}
\exp\!\left(-\frac{\Delta\varepsilon_0}{kT}\right),
$$

其中若把题给的 $D_e$ 视为势阱深度，则还需扣除零点能，

$$
\Delta\varepsilon_0 = D_0 = D_e - \frac{1}{2}hc\tilde\nu.
$$

并且

$$
q^\circ_{Na}=q^\circ_{\mathrm{trans}}(Na)\,q_{\mathrm{elec}}(Na),
\qquad
q^\circ_{Na_2}=q^\circ_{\mathrm{trans}}(Na_2)\,q_{\mathrm{rot}}(Na_2)\,q_{\mathrm{vib}}(Na_2)\,q_{\mathrm{elec}}(Na_2).
$$

各项写为：

$$
q^\circ_{\mathrm{trans}}(i)
=\left(\frac{2\pi m_i kT}{h^2}\right)^{3/2}\frac{V_m^\circ}{N_A},
\qquad
V_m^\circ=\frac{RT}{p^\circ},
$$

$$
q_{\mathrm{rot}}(Na_2)\approx \frac{T}{2\theta_{\mathrm{rot}}}
\quad(\text{同核双原子，}\sigma=2),
$$

$$
q_{\mathrm{vib}}(Na_2)
=\frac{\exp\!\left(-\theta_{\mathrm{vib}}/2T\right)}
{1-\exp\!\left(-\theta_{\mathrm{vib}}/T\right)},
$$

$$
q_{\mathrm{elec}}(Na)=g_{Na}=2,\qquad
q_{\mathrm{elec}}(Na_2)\approx 1.
$$

故可整理为

$$
K_p = \frac{
\left[q^\circ_{\mathrm{trans}}(Na)\,g_{Na}\right]^2
}{
q^\circ_{\mathrm{trans}}(Na_2)\,q_{\mathrm{rot}}(Na_2)\,q_{\mathrm{vib}}(Na_2)\,g_{Na_2}
}
\exp\!\left(-\frac{D_e}{kT}\right),
\quad g_{Na}=2,\ g_{Na_2}\approx 1.
$$

代入 $T=1000\ \mathrm{K}$、$D_0 = D_e - \frac{1}{2}hc\tilde\nu$ 以及题给各项后，得到

$$
\boxed{K_p(1000\ \mathrm{K}) \approx 2.44}
$$

这里 $K_p$ 取标准态，因此是无量纲的；若按教材把它写成压力形式，则对应数值也约为 $2.44\ \mathrm{bar}$。

---

## 32. $Cs \rightleftharpoons Cs^+ + e^-$

**题目翻译**

1. 写出 $Li$ 、 $Li^+$ 、 $Cs$ 、 $Cs^+$ 的基态项符号；
2. 由 $Cs$ 的第一电离能求 $2000 \ \mathrm{K}$ 时电离平衡的 $K_c$ ；
3. 若初始浓度为 $c_0$ 、电离度为 $\alpha$ ，证明在 $\alpha \ll 1$ 时 $\alpha = \sqrt{ K_c / c_0 }$ ，并求 $p = 0.1 \ \mathrm{bar}$ 、 $T = 2000 \ \mathrm{K}$ 时的 $\alpha$ 。

**解答**

### 32.1 基态项符号

- $Li : 1s^2 2s^1 \Rightarrow {}^2 S_{1/2}$
- $Li^+ : 1s^2 \Rightarrow {}^1 S_0$
- $Cs : [Xe] 6s^1 \Rightarrow {}^2 S_{1/2}$
- $Cs^+ : [Xe] \Rightarrow {}^1 S_0$

### 32.2 平衡常数

对反应

$$
Cs \rightleftharpoons Cs^+ + e^-,
$$

有

$$
K_c = \frac{ f_{Cs^+} f_e }{ f_{Cs} } \frac{1}{c^\circ}
\exp \left( - \frac{I_1}{kT} \right).
$$

其中

$$
I_1 = 3.893 \ \mathrm{eV}.
$$

代入电子和平动配分函数后得

$$
\boxed{ K_c(2000 \ \mathrm{K}) \approx 5.6 \times 10^{-11} \ \mathrm{mol \ dm^{-3}} }.
$$

### 32.3 电离度

若初始浓度为 $c_0$ ，平衡时

$$
[Cs] = c_0(1-\alpha), \qquad
[Cs^+] = [e^-] = c_0 \alpha.
$$

于是

$$
K_c = \frac{ (c_0 \alpha)^2 }{ c_0 (1-\alpha) }
= \frac{ c_0 \alpha^2 }{ 1-\alpha }.
$$

若 $\alpha \ll 1$ ，则

$$
K_c \approx c_0 \alpha^2,
$$

所以

$$
\boxed{ \alpha \approx \sqrt{ \frac{K_c}{c_0} } }.
$$

在 $p = 0.1 \ \mathrm{bar}$ 、 $T = 2000 \ \mathrm{K}$ 时，

$$
c_0 = \frac{p}{RT} \approx 6.01 \times 10^{-4} \ \mathrm{mol \ dm^{-3}}.
$$

故

$$
\alpha \approx \sqrt{ \frac{5.6 \times 10^{-11}}{6.01 \times 10^{-4}} }
\approx 3.0 \times 10^{-4}.
$$

即

$$
\boxed{ \alpha \approx 3.0 \times 10^{-4} }.
$$

这说明即使在 $2000 \ \mathrm{K}$ ， $Cs$ 蒸气在 $0.1 \ \mathrm{bar}$ 下仍只有极小部分被电离。

---

## 33. 同位素交换平衡 $H_2 + D_2 \rightleftharpoons 2HD$

**题目翻译**

利用平动、转动、振动配分函数，求 $800 \ \mathrm{K}$ 时

$$
H_2(g) + D_2(g) \rightleftharpoons 2HD(g)
$$

的 $K_c$ ，并评论结果。

**解答思路**

题目已给出

$$
K_c = \frac{ f_{HD}^2 }{ f_{H_2} f_{D_2} }\exp\left(-\frac{\Delta\varepsilon_{0}}{kT}\right).
$$

又因三者具有相同势能曲线，所以

$$
\Delta \varepsilon_0 = 0.
$$

故只需比较三项：

1. 平动质量因子；
2. 转动配分函数比值；
3. 振动配分函数比值。

### 33.1 约化质量

$$
\mu(H_2) = \frac{1 \times 1}{1+1} = 0.5 \ \mathrm{amu},
$$

$$
\mu(D_2) = \frac{2 \times 2}{2+2} = 1.0 \ \mathrm{amu},
$$

$$
\mu(HD) = \frac{1 \times 2}{1+2} = \frac{2}{3} \ \mathrm{amu}.
$$

### 33.2 标度关系

对相同势能曲线，

$$
\theta_{\mathrm{rot}} \propto \mu^{-1}, \qquad
\theta_{\mathrm{vib}} \propto \mu^{-1/2}.
$$

因此可由题给的 $H_2$ 数据直接求出 $D_2$ 与 $HD$ 的对应参数。

### 33.3 平动因子

由于

$$
f_{\mathrm{trans}} \propto m^{3/2},
$$

所以

$$
\frac{ f_{\mathrm{trans},HD}^2 }{ f_{\mathrm{trans},H_2} f_{\mathrm{trans},D_2} }
= \frac{ 3^3 }{ 2^{3/2} 4^{3/2} }
\approx 1.193.
$$

### 33.4 转动因子

高温下

$$
q_{\mathrm{rot}} \approx \frac{T}{\sigma \theta_{\mathrm{rot}}},
$$

其中 $\sigma(H_2) = \sigma(D_2) = 2$ ， $\sigma(HD)=1$ 。于是

$$
q_{\mathrm{rot}}(H_2) \approx \frac{800}{2 \times 85.3} = 4.689,
$$

$$
q_{\mathrm{rot}}(D_2) \approx \frac{800}{2 \times 42.65} = 9.379,
$$

$$
q_{\mathrm{rot}}(HD) \approx \frac{800}{63.975} = 12.505.
$$

故

$$
\frac{ q_{\mathrm{rot},HD}^2 }{ q_{\mathrm{rot},H_2} q_{\mathrm{rot},D_2} }
\approx 3.556.
$$

### 33.5 振动因子

必须用“从势阱底部计能量”的形式：

$$
q_{\mathrm{vib}} = \frac{ \exp(-\theta_{\mathrm{vib}}/2T) }{ 1-\exp(-\theta_{\mathrm{vib}}/T) }.
$$

代入得

$$
q_{\mathrm{vib}}(H_2) \approx 0.02057,
$$

$$
q_{\mathrm{vib}}(D_2) \approx 0.06441,
$$

$$
q_{\mathrm{vib}}(HD) \approx 0.03464.
$$

故

$$
\frac{ q_{\mathrm{vib},HD}^2 }{ q_{\mathrm{vib},H_2} q_{\mathrm{vib},D_2} }
\approx 0.9057.
$$

### 33.6 总平衡常数

于是

$$
K_c
= \frac{ f_{\mathrm{trans},HD}^2 }{ f_{\mathrm{trans},H_2} f_{\mathrm{trans},D_2} }
\frac{ q_{\mathrm{rot},HD}^2 }{ q_{\mathrm{rot},H_2} q_{\mathrm{rot},D_2} }
\frac{ q_{\mathrm{vib},HD}^2 }{ q_{\mathrm{vib},H_2} q_{\mathrm{vib},D_2} }
\approx 1.193 \times 3.556 \times 0.9057.
$$

即

$$
\boxed{ K_c(800 \ \mathrm{K}) \approx 3.84 }.
$$

**评论**

$K_c$ 明显大于 1，说明平衡偏向 $HD$ 。主要原因是同位素替换改变了转动对称数和零点能，从而使 $HD$ 在统计热力学上更有利。

---

## 34. 一般同位素交换 $A_2 + B_2 \rightleftharpoons 2AB$

**题目翻译**

若 $A$ 与 $B$ 是同一元素的两种同位素，并进一步假设它们质量足够接近，以至于可近似认为三种分子拥有相同质量、相同 $\theta_{\mathrm{rot}}$ 和相同 $\theta_{\mathrm{vib}}$ 。求

$$
A_2(g) + B_2(g) \rightleftharpoons 2AB(g)
$$

的 $K_c$ 。

**解答**

在这些近似下：

- 平动部分完全相消；
- 转动部分完全相消；
- 振动部分完全相消；
- 且 $\Delta \varepsilon_0 = 0$ 。

因此

$$
\boxed{ K_c = 1 }.
$$

**评论**

若把所有同位素效应都忽略，则体系不存在热力学偏向；真实体系中 $K_c$ 偏离 1 的来源正是质量差异引起的零点能、转动和振动统计差别。

---

## 35. 用动力学方法推导 Langmuir 等温式

**解答**

设表面共有 $M$ 个吸附位，已占据 $N$ 个，覆盖度为

$$
\theta = \frac{N}{M}.
$$

吸附速率正比于空位数与气体压强：

$$
r_{\mathrm{ads}} = k_a (M-N) p.
$$

脱附速率正比于已占据位数：

$$
r_{\mathrm{des}} = k_d N.
$$

平衡时两者相等：

$$
k_a (M-N) p = k_d N.
$$

整理得

$$
\frac{k_a}{k_d} = \frac{N}{(M-N)p}
= \frac{\theta}{(1-\theta)p}.
$$

定义

$$
K_{\mathrm{ads}} = \frac{k_a}{k_d},
$$

则

$$
\theta = \frac{ K_{\mathrm{ads}} p }{ 1 + K_{\mathrm{ads}} p }.
$$

**直线化方法**

由上式得

$$
\frac{p}{\theta} = \frac{1}{K_{\mathrm{ads}}} + p.
$$

故作图 $p/\theta$ 对 $p$ 应为直线：

- 斜率为 1；
- 截距为 $1/K_{\mathrm{ads}}$ 。

**Arrhenius 形式**

若

$$
k_a = A_a \exp(-E_a^{(\mathrm{ads})}/RT),
$$

$$
k_d = A_d \exp(-E_a^{(\mathrm{des})}/RT),
$$

则

$$
K_{\mathrm{ads}} = \frac{A_a}{A_d} \exp \left[ - \frac{ E_a^{(\mathrm{ads})} - E_a^{(\mathrm{des})} }{RT} \right].
$$

指数项实际上反映自由分子与吸附态之间的能量差。只有吸附伴随明显降能时， $K_{\mathrm{ads}}$ 才会显著大于 1，表面才会有明显覆盖。

---

## 36. 用统计热力学推导 Langmuir 等温式

**题目翻译（按原题 a-d）**

(a) 解释为什么把 $N$ 个不可分辨分子吸附到 $M$ 个可区分位点上的方式数为

$$
\frac{M!}{N!(M-N)!}.
$$

(b) 已知

$$
Q_N = q^N \times \frac{M!}{N!(M-N)!},
$$

证明

$$
A = kT\left[-N\ln q - M\ln M + N\ln N + (M-N)\ln(M-N)\right].
$$

并据此推导式(10.14)中给出的吸附相化学势 $\mu(\mathrm{ads})$ 。

(c) 令气相与吸附相化学势相等，推导式(10.15)中覆盖度 $\theta$ 的表达式。

(d) （较难）若吸附分子实际上是闭壳层原子，说明为何可取 $q=1$ 。再把式(10.15)中的 $\mu^\circ$ 用配分函数形式改写（注意自由原子与吸附原子基电子态能量差），并据此解释为什么只有当吸附原子能量显著低于自由原子时， $K_{\mathrm{ads}}$ 才会显著。

**解答**

### 36.1 (a) 排列数

表面有 $M$ 个可区分位点，每个位点至多容纳一个粒子。放入 $N$ 个不可分辨分子后，微观构型只取决于“哪 $N$ 个位点被占据”。

因此方式数就是从 $M$ 个位点中选 $N$ 个的组合数：

$$
\Omega = \binom{M}{N} = \frac{M!}{N!(M-N)!}.
$$

### 36.2 (b) 由 $Q_N$ 推导 $A$ 与 $\mu_{\mathrm{ads}}$

给定

$$
Q_N = q^N\frac{M!}{N!(M-N)!},
$$

于是

$$
\ln Q_N = N\ln q + \ln M! - \ln N! - \ln(M-N)!.
$$

由

$$
A=-kT\ln Q_N,
$$

并用 Stirling 近似 $\ln n!\approx n\ln n-n$（常数项在后续求导中抵消），得

$$
A = kT\left[-N\ln q - M\ln M + N\ln N + (M-N)\ln(M-N)\right].
$$

这正是题目要求式子。

再求吸附相化学势（保持 $T,M$ 不变）：

$$
\mu_{\mathrm{ads}}
=\left(\frac{\partial A}{\partial N}\right)_{T,M}
=-kT\ln q + kT\ln\frac{N}{M-N}.
$$

令覆盖度 $\theta=N/M$ ，则

$$
\boxed{
\mu_{\mathrm{ads}}=-kT\ln q + kT\ln\frac{\theta}{1-\theta}
}
$$

即为式(10.14)形式。

### 36.3 (c) 由化学势相等得到 Langmuir 等温式

平衡条件：

$$
\mu_{\mathrm{gas}}=\mu_{\mathrm{ads}}.
$$

对理想气体可写成

$$
\mu_{\mathrm{gas}} = \mu^\circ(T)+kT\ln p
$$

（若严格写无量纲应为 $\ln(p/p^\circ)$ ，这里把标准态并入 $\mu^\circ$ ）。代入上式：

$$
\mu^\circ + kT\ln p
= -kT\ln q + kT\ln\frac{\theta}{1-\theta}.
$$

整理得

$$
\frac{\theta}{1-\theta} = q\,p\,\exp\!\left(\frac{\mu^\circ}{kT}\right)
\equiv K_{\mathrm{ads}}p.
$$

因此

$$
\boxed{\theta = \frac{K_{\mathrm{ads}}p}{1+K_{\mathrm{ads}}p}}
$$

这就是式(10.15)（Langmuir 等温式）。

### 36.4 (d) 闭壳层原子时 $q\approx 1$ 与 $K_{\mathrm{ads}}$ 的物理意义

1. 对闭壳层原子，低能可及的内部激发态很少，室温附近几乎都在基态，因此吸附态内部配分函数常可近似

$$
q\approx 1.
$$

2. 把式(10.15)中的标准化学势写成配分函数形式。对理想气体原子（每粒子）有

$$
\mu_{\mathrm{gas}}
=kT\ln\!\left[\frac{p\,\Lambda^3}{kT\,q_{\mathrm{int}}^{\mathrm{gas}}}\right],
$$

其中 $\Lambda=h/\sqrt{2\pi mkT}$ 为热波长， $q_{\mathrm{int}}^{\mathrm{gas}}$ 是气相内部配分函数。

与

$$
\mu_{\mathrm{ads}}=-kT\ln q_{\mathrm{ads}}+kT\ln\frac{\theta}{1-\theta}
$$

相等后可得

$$
\frac{\theta}{1-\theta}=K_{\mathrm{ads}}p,
\qquad
K_{\mathrm{ads}}=\frac{q_{\mathrm{ads}}\Lambda^3}{kT\,q_{\mathrm{int}}^{\mathrm{gas}}}.
$$

3. 若显式分离基电子态能量（零点）

$$
q_{\mathrm{ads}}=\tilde q_{\mathrm{ads}}\,e^{-\varepsilon_{0,\mathrm{ads}}/kT},
\qquad
q_{\mathrm{int}}^{\mathrm{gas}}=\tilde q_{\mathrm{gas}}\,e^{-\varepsilon_{0,\mathrm{gas}}/kT},
$$

则

$$
K_{\mathrm{ads}}
\propto
\exp\!\left[-\frac{\varepsilon_{0,\mathrm{ads}}-\varepsilon_{0,\mathrm{gas}}}{kT}\right]
=\exp\!\left(-\frac{\Delta\varepsilon_0}{kT}\right).
$$

当吸附态显著更稳定（ $\varepsilon_{0,\mathrm{ads}}\ll\varepsilon_{0,\mathrm{gas}}$ ，即 $\Delta\varepsilon_0\ll0$ ）时，指数因子才会很大，故 $K_{\mathrm{ads}}$ 才显著；若两者能量差不大， $K_{\mathrm{ads}}$ 通常不会很大。

---

## 37. 三体基元反应的三级速率常数

**解答**

仿照二体反应的过渡态理论，对基元反应

$$
A + B + C \rightarrow \text{products}
$$

若三者共同形成过渡态，则

$$
k_{3rd} = \frac{kT}{h} \frac{ f^\ddagger }{ f_A f_B f_C }
\exp \left( - \frac{ \Delta \varepsilon_0^\ddagger }{kT} \right),
$$

并还需包含与标准浓度有关的体积因子，使其最终量纲为

$$
\mathrm{(concentration)^{-2} \ time^{-1}}.
$$

若用 $\mathrm{mol \ dm^{-3}}$ 作浓度单位，则三级速率常数单位是

$$
\boxed{ \mathrm{dm^6 \ mol^{-2} \ s^{-1}} }.
$$

与二级反应相比，只是多了一个反应物，因此多出一个浓度倒数量纲。

---

## 38. 过渡态理论计算 $D + H_2 \rightarrow DH + H$

**解答**

在 $T=1000\ \mathrm{K}$ ，用过渡态理论

$$
k_{2nd} = \frac{k_B T}{h} \frac{ f^\ddagger }{ f_D f_{H_2} }
\exp\!\left(-\frac{\Delta \varepsilon_0^\ddagger}{RT}\right).
$$

已知

$$
\Delta \varepsilon_0^\ddagger = 40.3\ \mathrm{kJ\ mol^{-1}}.
$$

下面把比值 $f^\ddagger/(f_D f_{H_2})$ 分成平动、转动、振动、电子四部分。

### 38.1 平动部分

采用每单位体积单分子平动配分函数

$$
f_{\mathrm{trans}} = \left(\frac{2\pi m k_B T}{h^2}\right)^{3/2}.
$$

因此

$$
\frac{f_{\mathrm{trans}}^\ddagger}{f_{\mathrm{trans},D}f_{\mathrm{trans},H_2}}
=\left(\frac{h^2}{2\pi\mu k_B T}\right)^{3/2},
$$

其中

$$
\mu = \frac{m_D m_{H_2}}{m_D+m_{H_2}}.
$$

取

$$
m_H=1.007825\,u,\quad m_D=2.014102\,u,\quad m_{H_2}=2m_H,
$$

$$
1u=1.660539\times10^{-27}\ \mathrm{kg},
$$

得

$$
\mu = 1.341\times10^{-27}\ \mathrm{kg}.
$$

所以

$$
\boxed{
\frac{f_{\mathrm{trans}}^\ddagger}{f_{\mathrm{trans},D}f_{\mathrm{trans},H_2}}
=1.664\times10^{-31}\ \mathrm{m^3}
}.
$$

### 38.2 转动部分

#### (1) $H_2$ 反应物

线型刚性转子高温近似

$$
q_{\mathrm{rot}} = \frac{T}{\sigma\theta_{\mathrm{rot}}},
\qquad
  \theta_{\mathrm{rot}}=\frac{h^2}{8\pi^2 I k_B}.
$$

对 $H_2$ ：$r=0.741\ \mathrm{\AA}$ ，$\sigma=2$ ，可得

$$
	\theta_{\mathrm{rot}}(H_2)\approx 87.66\ \mathrm{K},
\qquad
q_{\mathrm{rot}}(H_2)=\frac{1000}{2\times 87.66}=5.704.
$$

#### (2) 过渡态 $[D\cdots H\cdots H]^\ddagger$

线型三原子，取坐标

$$
x_D=0,\quad x_{H^{(1)}}=0.929\ \mathrm{\AA},\quad x_{H^{(2)}}=1.858\ \mathrm{\AA}.
$$

质心位置

$$
x_{\mathrm{cm}}=\frac{2x_D+x_{H^{(1)}}+x_{H^{(2)}}}{4}=0.69675\ \mathrm{\AA}.
$$

转动惯量

$$
I^\ddagger=\sum_i m_i(x_i-x_{\mathrm{cm}})^2
=3.94\times10^{-47}\ \mathrm{kg\ m^2}.
$$

过渡态非对称，$\sigma=1$ ，故

$$
	\theta_{\mathrm{rot}}^\ddagger=\frac{h^2}{8\pi^2 I^\ddagger k_B}
\approx 10.14\ \mathrm{K},
$$

$$
q_{\mathrm{rot}}^\ddagger = \frac{1000}{10.14}=98.59.
$$

故转动比值

$$
\boxed{
\frac{q_{\mathrm{rot}}^\ddagger}{q_{\mathrm{rot}}(H_2)}
=17.28
}.
$$

### 38.3 振动部分

与给定 $\Delta\varepsilon_0^\ddagger$ 的写法一致，取

$$
q_{\mathrm{vib}}=\frac{1}{1-e^{-\theta_{\mathrm{vib}}/T}},
\qquad
  \theta_{\mathrm{vib}}=\frac{hc\tilde\nu}{k_B}=1.4387769\,\tilde\nu\ (\mathrm{K}).
$$

#### (1) $H_2$

$$
	\tilde\nu=4401\ \mathrm{cm^{-1}}\Rightarrow
	\theta_{\mathrm{vib}}=6331.7\ \mathrm{K},
$$

$$
q_{\mathrm{vib}}(H_2)=\frac{1}{1-e^{-6331.7/1000}}=1.002.
$$

#### (2) 过渡态

稳定振动模：$1708\ \mathrm{cm^{-1}}$ 和 $861\ \mathrm{cm^{-1}}$（后者二重简并），
沿反应坐标的虚频不计入。

$$
q_{\mathrm{vib}}^\ddagger
=\frac{1}{1-e^{-2457.4/1000}}
\left(\frac{1}{1-e^{-1238.8/1000}}\right)^2
=2.168.
$$

故振动比值

$$
\boxed{
\frac{q_{\mathrm{vib}}^\ddagger}{q_{\mathrm{vib}}(H_2)}
=2.164
}.
$$

### 38.4 电子部分

取 $g_e(D)=2$ ，$g_e(H_2)=1$ ，$g_e^\ddagger=2$ ，则

$$
\frac{g_e^\ddagger}{g_e(D)g_e(H_2)}=1.
$$

### 38.5 合并配分函数比值

$$
\frac{f^\ddagger}{f_D f_{H_2}}
=\frac{f_{\mathrm{trans}}^\ddagger}{f_{\mathrm{trans},D}f_{\mathrm{trans},H_2}}
\frac{q_{\mathrm{rot}}^\ddagger}{q_{\mathrm{rot}}(H_2)}
\frac{q_{\mathrm{vib}}^\ddagger}{q_{\mathrm{vib}}(H_2)}
\frac{g_e^\ddagger}{g_e(D)g_e(H_2)}
$$

$$
=\left(1.664\times10^{-31}\ \mathrm{m^3}\right)\times 17.28 \times 2.164
=\boxed{6.224\times10^{-30}\ \mathrm{m^3}}.
$$

### 38.6 代入 Eyring 公式并给出单位

先算前因子与指数项：

$$
\frac{k_B T}{h}=2.084\times10^{13}\ \mathrm{s^{-1}},
$$

$$
\exp\!\left(-\frac{\Delta\varepsilon_0^\ddagger}{RT}\right)
=\exp\!\left(-\frac{40.3\times10^3}{8.314\times1000}\right)
=7.87\times10^{-3}.
$$

所以

$$
k_{2nd}
=\frac{k_B T}{h}\frac{f^\ddagger}{f_D f_{H_2}}
\exp\!\left(-\frac{\Delta\varepsilon_0^\ddagger}{RT}\right)
$$

$$
=\left(2.084\times10^{13}\right)
\left(6.224\times10^{-30}\ \mathrm{m^3}\right)
\left(7.87\times10^{-3}\right)
$$

$$
=\boxed{1.02\times10^{-18}\ \mathrm{m^3\ molecule^{-1}\ s^{-1}}}.
$$

换算成常见化学动力学单位

$$
1\ \mathrm{m^3\ molecule^{-1}\ s^{-1}}
=10^3 N_A\ \mathrm{dm^3\ mol^{-1}\ s^{-1}},
$$

故

$$
\boxed{k_{2nd}(1000\ \mathrm{K})
=6.13\times10^8\ \mathrm{dm^3\ mol^{-1}\ s^{-1}}}.
$$

即该反应在 1000 K 下给出一个数量级较大的二级速率常数，但仍低于无势垒碰撞极限。

---

## 39. 两原子反应 $A + B$ 的过渡态理论速率常数

**解答**

对反应

$$
A + B \rightarrow [AB]^\ddagger \rightarrow \text{products},
$$

过渡态理论给出

$$
k_{2nd} = \frac{kT}{h} \frac{ f^\ddagger }{ f_A f_B }\exp \left( - \frac{ \Delta \varepsilon_0^\ddagger }{kT} \right).
$$

对原子 $A$ 与 $B$ ，内部配分函数很简单；过渡态可视作一条线型双原子“分子”，其内部自由度主要是转动。于是

$$
f^\ddagger \propto \left( \frac{2 \pi \mu kT}{h^2} \right)^{3/2} q_{\mathrm{rot}}^\ddagger,
$$

而

$$
q_{\mathrm{rot}}^\ddagger \propto \frac{8 \pi^2 I kT}{\sigma h^2}
\propto \mu R^2 T.
$$

因此最终得到的速率常数会含有碰撞截面尺度 $\pi R^2$ 与平均相对速率尺度 $\sqrt{ kT / \mu }$ 。这与简单碰撞理论

$$
k_{\mathrm{coll}} \sim \pi R^2 \sqrt{ \frac{8kT}{\pi \mu} }
\exp \left( - \frac{E_a}{kT} \right)
$$

在结构上是一致的。

**如何协调两者**

- 碰撞理论把“有足够能量且几何碰上”当作反应条件；
- 过渡态理论把“到达分界面并越过自由能垒”作为条件。

因此两者都体现了“碰撞频率 $\times$ 指数垒因子”，只是对取向和势能面的处理细致程度不同。

---

## 40. 非线型过渡态的立体因子

**解答**

与 Example 16 的线型过渡态相比，非线型过渡态拥有更多转动自由度，因此可接受的取向相空间更大。于是从统计上看，非线型过渡态对应的立体因子一般会：

- 比严格线型过渡态更大；
- 更接近 1；
- 表明对取向要求较宽松。

其根本原因是：线型过渡态只允许非常狭窄的相对定向，而非线型过渡态对应更大的角空间。

---

## 41. ${}^{12}C \rightarrow {}^{13}C$ 的动力学同位素效应

**解答**

${}^{12}C$ 与 ${}^{13}C$ 的质量相对变化仅约 $8\%$ ，且碳原子通常并非高频伸缩模中最敏感的轻原子，因此：

- 对振动零点能的影响较小；
- 对速率常数的影响通常远弱于 $H/D$ 取代。

所以碳同位素 KIE 一般只有几个百分点，常见量级是

$$
\boxed{ k_{12} / k_{13} \sim 1.01 \text{ 到 } 1.05 }.
$$

这属于典型的“小同位素效应”。

---

## 42. Eyring 方程、活化焓与活化熵

**解答**

### 42.1 与活化焓、活化熵的关系

Eyring 方程可写为

$$
k_{2nd} = \frac{kT}{c^\circ h} K^\ddagger.
$$

又有

$$
\Delta_r G^{\circ,\ddagger} = \Delta_r H^{\circ,\ddagger} - T \Delta_r S^{\circ,\ddagger},
$$

以及

$$
K^\ddagger = \exp \left( - \frac{ \Delta_r G^{\circ,\ddagger} }{RT} \right).
$$

故

$$
k_{2nd}
= \frac{kT}{c^\circ h}
\exp \left( \frac{ \Delta_r S^{\circ,\ddagger} }{R} \right)
\exp \left( - \frac{ \Delta_r H^{\circ,\ddagger} }{RT} \right).
$$

与 Arrhenius 形式

$$
k = A \exp(-E_a/RT)
$$

比较，在溶液中有近似关系

$$
\boxed{ E_a \approx \Delta_r H^{\circ,\ddagger} + RT },
$$

$$
\boxed{ A \approx \frac{kT}{c^\circ h} \exp \left( \frac{ \Delta_r S^{\circ,\ddagger} }{R} \right) }.
$$

### 42.2 线性作图法

把 Eyring 方程改写为

$$
\ln \left( \frac{k}{T} \right)
= \ln \left( \frac{k}{c^\circ h} \right)
+ \frac{ \Delta_r S^{\circ,\ddagger} }{R}
- \frac{ \Delta_r H^{\circ,\ddagger} }{RT}.
$$

因此作图

$$
\ln(k/T) \text{ 对 } 1/T
$$

应得到直线：

- 斜率为 $- \Delta_r H^{\circ,\ddagger} / R$
- 截距为 $\ln(k/c^\circ h) + \Delta_r S^{\circ,\ddagger}/R$

### 42.3 对题中 $SN2$ 数据做线性拟合

把表中温度换成 K：

$$
T = 298.15,\ 307.75,\ 317.65,\ 328.35,\ 337.95 \ \mathrm{K}.
$$

速率常数为

$$
k = 6.45,\ 16.4,\ 41.0,\ 106,\ 215
\times 10^{-5} \ \mathrm{dm^3 \ mol^{-1} \ s^{-1}}.
$$

对 $\ln(k/T)$ 与 $1/T$ 线性拟合，得到

$$
\text{slope} \approx -8622 \ \mathrm{K},
$$

$$
\text{intercept} \approx 13.576.
$$

因此

$$
\Delta_r H^{\circ,\ddagger} = - R \times \text{slope}
\approx 71.7 \ \mathrm{kJ \ mol^{-1}}.
$$

由截距得

$$
\Delta_r S^{\circ,\ddagger}
= R \left[ \text{intercept} - \ln \left( \frac{k_B}{h} \right) \right]
\approx -84.7 \ \mathrm{J \ mol^{-1} \ K^{-1}}.
$$

再由

$$
E_a \approx \Delta_r H^{\circ,\ddagger} + RT
$$

可得

$$
E_a \approx 74.3 \ \mathrm{kJ \ mol^{-1}}.
$$

因此

$$
\boxed{ \Delta_r H^{\circ,\ddagger} \approx 71.7 \ \mathrm{kJ \ mol^{-1}} }
$$

$$
\boxed{ \Delta_r S^{\circ,\ddagger} \approx -84.7 \ \mathrm{J \ mol^{-1} \ K^{-1}} }
$$

$$
\boxed{ E_a \approx 74.3 \ \mathrm{kJ \ mol^{-1}} }.
$$

负的活化熵与双分子 $SN2$ 反应形成较有序过渡态的图像完全一致。

---

## 43. 压力依赖与活化体积

**解答**

### 43.1 定义

由

$$
k_{2nd} = \frac{kT}{c^\circ h} K^\ddagger
$$

和

$$
\Delta_r G^{\circ,\ddagger} = -RT \ln K^\ddagger
$$

可得

$$
\left( \frac{\partial \ln k}{\partial p} \right)_T
= - \frac{1}{RT} \left( \frac{\partial \Delta_r G^{\circ,\ddagger} }{\partial p} \right)_T
= - \frac{ \Delta_r V^{\circ,\ddagger} }{RT }.
$$

因此

$$
\boxed{
\Delta_r V^{\circ,\ddagger}
= - RT \left( \frac{\partial \ln k}{\partial p} \right)_T
}.
$$

### 43.2 作图法

作图 $\ln k$ 对 $p$ ：

- 斜率为 $- \Delta_r V^{\circ,\ddagger} / RT$
- 由此可求活化体积

### 43.3 物理意义

- 若压强升高使速率增大，则斜率为正， $\Delta_r V^{\circ,\ddagger} < 0$ ，说明过渡态更紧凑。
- 若压强升高使速率减小，则 $\Delta_r V^{\circ,\ddagger} > 0$ ，说明过渡态更疏松。

该概念主要对溶液反应有意义，因为液相中压缩性、溶剂化重排和体积变化可直接影响自由能；对稀薄气相反应，这种描述通常不如势能面与碰撞动力学直观。

### 43.4 对题中数据做估算

因为表中给的是相对速率 $k(p)/k(p=1)$ ，所以可直接对

$$
\ln \left[ \frac{k(p)}{k(1)} \right]
$$

与 $p$ 作图。

以 $298 \ \mathrm{K}$ 线性拟合得到：

- 对 [R1]
  $$
  \Delta_r V^{\circ,\ddagger} \approx -9.7 \ \mathrm{cm^3 \ mol^{-1}}
  $$
- 对 [R2]
  $$
  \Delta_r V^{\circ,\ddagger} \approx +8.5 \ \mathrm{cm^3 \ mol^{-1}}
  $$

因此

$$
\boxed{ \Delta_r V^{\circ,\ddagger}([R1]) \approx -9.7 \ \mathrm{cm^3 \ mol^{-1}} }
$$

$$
\boxed{ \Delta_r V^{\circ,\ddagger}([R2]) \approx +8.5 \ \mathrm{cm^3 \ mol^{-1}} }.
$$

物理上这表示：

- [R1] 的过渡态比反应物更紧凑，受压有利；
- [R2] 的过渡态更膨胀，受压不利。

---

## 44. 由 $\Delta_r S^{\circ,\ddagger}$ 与 $\Delta_r V^{\circ,\ddagger}$ 判断机理

**解答**

判断原则：

- $\Delta_r S^{\circ,\ddagger} < 0$ ：过渡态更有序，常见于缔合型机理；
- $\Delta_r S^{\circ,\ddagger} > 0$ ：过渡态更松散，常见于解离型机理；
- $\Delta_r V^{\circ,\ddagger} < 0$ ：过渡态更紧凑；
- $\Delta_r V^{\circ,\ddagger} > 0$ ：过渡态更膨胀。

因此表中数据可作如下解释：

- $Cr(NH_3)_5(HCONH_2)^{3+}$ 的取代反应： $\Delta_r S^{\circ,\ddagger}$ 与 $\Delta_r V^{\circ,\ddagger}$ 都偏负，支持缔合特征较强。
- 对应的 $Co$ 体系：两者转为正或更不负，说明更偏向解离型。
- $Co(en)_2(OH)(Cl)^+$ 的水取代：正的 $\Delta_r S^{\circ,\ddagger}$ 倾向支持解离机理。
- $Pt(PEt_3)_2(Cl)(Me)^+ + Br^-$ ：很大的负熵支持典型缔合型取代。
- 表中有机反应若表现为较大负体积或负熵，通常说明电荷离域或拥挤的双分子过渡态；若两者为正，则更可能经历键断裂主导的步骤。

---

## 45. 由桥梁关系推导理想气体压强

**解答**

### 45.1 Helmholtz 自由能

对 $N$ 个互不相互作用、不可分辨粒子，

$$
Q_N = \frac{q^N}{N!}.
$$

因此

$$
A = -kT \ln Q_N
= -NkT \ln q + kT \ln N!.
$$

用 Stirling 公式

$$
\ln N! \approx N \ln N - N
$$

即得

$$
\boxed{
A = -NkT \ln q + kT ( N \ln N - N )
}.
$$

### 45.2 单原子气体压强

若气体只有平动自由度，则

$$
q = q_{\mathrm{trans}} \propto V.
$$

于是

$$
p = - \left( \frac{\partial A}{\partial V} \right)_T
= NkT \left( \frac{\partial \ln q_{\mathrm{trans}} }{\partial V} \right)_T
= \frac{NkT}{V}.
$$

故

$$
\boxed{ pV = NkT }.
$$

这就是理想气体方程。

### 45.3 双原子气体

对双原子分子，

$$
q = q_{\mathrm{trans}} q_{\mathrm{rot}} q_{\mathrm{vib}} q_{\mathrm{elec}}.
$$

其中只有 $q_{\mathrm{trans}}$ 含体积 $V$ ，因此对压强求导时其余因子不贡献体积导数，结果仍然是

$$
\boxed{ p = \frac{NkT}{V} }.
$$

所以内部自由度不改变理想气体压强表达式。

---

## 46. $500 \ \mathrm{K}$ 时 Si 原子各电子能级布居

**解答**

由第 12 题的能级与简并度，

$$
P_j = \frac{ g_j \exp(-\varepsilon_j/kT) }{ q_{\mathrm{elec}} }.
$$

在 $T = 500 \ \mathrm{K}$ 时， $q_{\mathrm{elec}} \approx 6.050$ 。各能级布居分数为：

| 能级 | 布居分数 |
|---|---:|
| ${}^3P_0$ | $0.1653$ |
| ${}^3P_1$ | $0.3984$ |
| ${}^3P_2$ | $0.4363$ |
| ${}^1D_2$ | $1.12 \times 10^{-8}$ |
| ${}^1S_0$ | $9.67 \times 10^{-21}$ |

因此在 $500 \ \mathrm{K}$ 下几乎全部布居都集中在 ${}^3P_J$ 多重态的三个细结构能级上。

---

## 47. 最概然转动量子数

**解答**

某一转动态的布居正比于

$$
N_J \propto (2J+1) \exp \left[ - \frac{B J(J+1)}{kT} \right].
$$

把 $J$ 视为连续变量，令

$$
\frac{d}{dJ} \ln N_J = 0,
$$

得

$$
\frac{2}{2J+1} - \frac{B (2J+1)}{kT} = 0.
$$

因此

$$
(2J+1)^2 = \frac{2kT}{B}.
$$

故最概然 $J$ 的连续近似为

$$
\boxed{
J_{\max} \approx \frac{1}{2} \left( \sqrt{ \frac{2kT}{B} } - 1 \right)
}.
$$

若用波数常数 $\tilde{B}$ ，则

$$
\boxed{
J_{\max} \approx \frac{1}{2} \left( \sqrt{ \frac{2T}{\theta_{\mathrm{rot}}} } - 1 \right)
}.
$$

### 47.1 对 HCl，若最概然级为 $J = 3$

已知 $\tilde{B} = 10.59 \ \mathrm{cm^{-1}}$ ，故

$$
\theta_{\mathrm{rot}} = 1.4387769 \times 10.59 \approx 15.23 \ \mathrm{K}.
$$

令连续极值落在 $J = 3$ ，则

$$
T \approx \frac{\theta_{\mathrm{rot}} (2J+1)^2}{2}
= \frac{15.23 \times 7^2}{2}
\approx 373 \ \mathrm{K}.
$$

因此

$$
\boxed{ T \approx 373 \ \mathrm{K} }.
$$

### 47.2 若要使 $J = 4$ 成为最概然级

对应温度约为

$$
T \approx \frac{15.23 \times 9^2}{2} \approx 617 \ \mathrm{K}.
$$

故温度需升高

$$
\Delta T \approx 617 - 373 \approx 244 \ \mathrm{K}.
$$

即

$$
\boxed{ \Delta T \approx 244 \ \mathrm{K} }.
$$

---

## 48. $N_2$ 在 $1 \ \mathrm{cm^3}$ 中可及平动能级数

**解答**

三维箱中，能量在 $0$ 到 $\varepsilon$ 之间的平动能级数为

$$
W(\varepsilon) = \frac{4 \pi V}{3} \left( \frac{2m}{h^2} \right)^{3/2} \varepsilon^{3/2}.
$$

令 $\varepsilon = kT$ ，对 $N_2$ 、 $T = 298 \ \mathrm{K}$ 、 $V = 1 \ \mathrm{cm^3} = 10^{-6} \ \mathrm{m^3}$ ，得

$$
W(0 \to kT) \approx 1.08 \times 10^{26}.
$$

样品中的粒子数为

$$
N = \frac{pV}{kT}
\approx \frac{ (1.0 \times 10^5)(10^{-6}) }{ (1.380649 \times 10^{-23})(298) }
\approx 2.43 \times 10^{19}.
$$

故

$$
\frac{W}{N} \approx 4.44 \times 10^6.
$$

也就是说，可及平动能级数比粒子数大约多六个数量级。

**为什么这很重要**

若可及能级远多于粒子数：

- 各粒子可以分散占据大量不同量子态；
- Maxwell-Boltzmann 统计近似才成立得很好；
- 不会出现“态数不够、必须大量重复占据同一量子态”的量子简并效应。

因此常温常压下气体平动行为近似经典是有根本统计依据的。

---

## 49. 二维箱中的态密度

**解答**

题目已给出二维箱中，能量在 $0$ 到 $\varepsilon$ 之间的态数为

$$
W_{2D}(\varepsilon) = \frac{2 \pi m A \varepsilon}{h^2}.
$$

态密度定义为

$$
D(\varepsilon) = \frac{dW}{d\varepsilon}.
$$

故

$$
\boxed{
D_{2D}(\varepsilon) = \frac{2 \pi m A}{h^2}
}.
$$

**评论**

二维自由粒子的态密度与能量无关，这是二维体系非常重要的一个特征；它与三维体系中 $D(\varepsilon) \propto \varepsilon^{1/2}$ 的结果明显不同。
