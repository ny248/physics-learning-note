# 量子論は何を変えたのか――シュレーディンガー方程式から場の量子論まで

量子論は、「小さな物体は不思議な動きをする」という話だけではありません。

古典物理学では説明できなかった実験事実を出発点として、**状態とは何か、測定値はどう決まるか、時間発展をどう表すか**を作り直した理論です。その考えを特殊相対論と両立させると、粒子を基本とする見方から、粒子を生み出したり消したりできる「場」を基本とする見方へ進むことになります。

この記事では、その論理を次の順にたどります。

1. 古典物理学では説明できない実験事実
2. 状態・観測量・確率を定める量子力学の公理
3. シュレーディンガー方程式と具体的な計算
4. 交換関係と不確定性原理
5. 特殊相対論を課したときに現れる反粒子
6. 粒子数の変化を扱う場の量子論
7. 対称性から電磁相互作用を構成する量子電磁気学
8. 繰り込みと標準模型への接続

中心にある方程式を先に並べると、量子論の発展は次の流れに要約できます。

$$
i\hbar\frac{\partial\psi}{\partial t}
=\hat H\psi
\quad\longrightarrow\quad
\left(i\hbar\gamma^\mu\partial_\mu-mc\right)\psi=0
\quad\longrightarrow\quad
\mathcal L_{\mathrm{QED}}
=
\bar\psi(i\gamma^\mu D_\mu-m)\psi
-\frac14F_{\mu\nu}F^{\mu\nu}.
$$

最初の式は非相対論的な一粒子の時間発展、二つ目は相対論的な電子の方程式、三つ目は電子・陽電子と光子の生成・消滅まで含む量子電磁気学を表します。

---

## 1. 古典物理学はどこで行き詰まったのか

19世紀末までに、物体の運動はニュートン力学、電気・磁気・光はマクスウェル電磁気学によって記述できるようになっていました。もし同じ理論を原子や電子にもそのまま適用できるなら、新しい力学は必要ありません。

しかし、微視的な世界では少なくとも三つの重大な不一致が現れました。

### 1.1 黒体放射――高い振動数でエネルギーが発散する

黒体とは、入射した電磁波を完全に吸収し、温度に応じた熱放射を出す理想化された物体です。温度を $${T}$$、電磁波の振動数を $${\nu}$$ とすると、古典論が予測する単位体積・単位振動数あたりのエネルギー密度は

$$
u_{\mathrm{RJ}}(\nu,T)
=
\frac{8\pi\nu^2}{c^3}k_{\mathrm B}T
$$

です。ここで $${c}$$ は光速、$${k_{\mathrm B}}$$ はボルツマン定数です。

この式を全振動数について積分すると、

$$
\int_0^\infty u_{\mathrm{RJ}}(\nu,T)\,d\nu
=\infty
$$

となります。つまり古典論は、熱平衡にある物体が高振動数の電磁波へ無限のエネルギーを渡すと予測してしまいます。実際のスペクトルは高振動数側で減衰し、プランクの式

$$
u_{\mathrm P}(\nu,T)
=
\frac{8\pi h\nu^3}{c^3}
\frac{1}{e^{h\nu/(k_{\mathrm B}T)}-1}
$$

で記述されます。

この式を得るには、振動数 $${\nu}$$ の電磁場がエネルギーを連続的に受け渡すのではなく、

$$
E=h\nu
$$

を単位として受け渡すと仮定する必要がありました。$${h}$$ はプランク定数です。

### 1.2 光電効果――光の強さだけでは電子を放出できない

金属へ光を当てると、電子が飛び出すことがあります。古典的な波の描像だけなら、強い光を長時間当てるほど電子へ多くのエネルギーを渡せるはずです。

ところが実験では、電子を放出するために最低限必要な振動数 $${\nu_0}$$ が存在します。放出された電子の最大運動エネルギーは

$$
K_{\max}=h\nu-\Phi
$$

となります。$${\Phi}$$ は金属から電子を取り出すために必要な仕事関数です。

光を強くすると主に放出電子の個数が増えますが、電子一個の最大運動エネルギーを決めるのは振動数です。この結果は、光が一個あたり $${h\nu}$$ のエネルギーをもつ量子として物質と相互作用することを示します。

### 1.3 原子スペクトル――原子のエネルギーは連続ではない

水素原子が放出・吸収する光の波長は、任意の値をとりません。観測される波長 $${\lambda}$$ は、リュードベリ定数 $${R}$$ を用いて

$$
\frac{1}{\lambda}
=
R\left(\frac{1}{m^2}-\frac{1}{n^2}\right),
\qquad n>m
$$

と整理できます。

さらに古典電磁気学によれば、加速度 $${a}$$ をもつ電荷は

$$
P=\frac{e^2a^2}{6\pi\varepsilon_0c^3}
$$

の電力を放射します。原子核のまわりを回る電子を古典的な荷電粒子と考えると、電子は放射によってエネルギーを失い、原子核へ落ち込むはずです。しかし実際の原子は安定です。

原子が特定のエネルギー $${E_n}$$ だけをもち、状態間の遷移で

$$
h\nu=E_n-E_m
$$

を満たす光だけを放出・吸収すると考えれば、線スペクトルを説明できます。

以上の実験事実が否定したのは、単なる個別の公式ではありません。微視的な世界では、次の三つを古典力学とは異なる形で定め直す必要があります。

- 系の**状態**を何で表すか
- 測定する**物理量**を何で表すか
- 状態の**時間発展**をどう定めるか

---

## 2. 量子力学は状態と測定をどう表すのか

量子力学の基本構造は、次の三つの対応にまとめられます。

$$
\boxed{
\text{状態}\leftrightarrow|\psi\rangle,\qquad
\text{物理量}\leftrightarrow\hat A,\qquad
\text{確率}\leftrightarrow|\langle a|\psi\rangle|^2
}
$$

ここで $${|\psi\rangle}$$ は状態ベクトル、$${\hat A}$$ は
物理量を表す演算子、$${|a\rangle}$$ は $${\hat A}$$ の固有状態です。
順に定義します。

### 2.1 状態は複素ベクトルで表す

量子系の状態は、複素ヒルベルト空間 $${\mathcal H}$$ のベクトル $${|\psi\rangle}$$ で表します。ヒルベルト空間とは、内積が定義され、その内積から定まる距離について極限操作を行える複素ベクトル空間です。

状態は

$$
\langle\psi|\psi\rangle=1
$$

となるように正規化します。$${|\psi\rangle}$$ と $${e^{i\theta}|\psi\rangle}$$ は、全体に共通する位相が違うだけなので、同じ物理状態を表します。

量子論で複素数が必要なのは、複素振幅の位相差が干渉を決めるからです。二つの経路に対応する振幅を $${\psi_1,\psi_2}$$ とすると、確率は

$$
|\psi_1+\psi_2|^2
=
|\psi_1|^2+|\psi_2|^2
+2\operatorname{Re}(\psi_1^*\psi_2)
$$

です。最後の干渉項は、確率そのものを足しただけでは現れません。

### 2.2 物理量は自己共役演算子で表す

位置、運動量、エネルギーなどの物理量は、状態ベクトルに作用する自己共役演算子 $${\hat A}$$ で表します。

$$
\hat A^\dagger=\hat A
$$

という自己共役性により、測定値に対応する固有値は実数になります。固有値 $${a}$$ と固有状態 $${|a\rangle}$$ は

$$
\hat A|a\rangle=a|a\rangle
$$

で定義されます。

ここで、状態と物理量を区別することが重要です。$${|\psi\rangle}$$ は「系をどう準備したか」を表し、$${\hat A}$$ は「測定装置が何を問うか」を表します。同じ状態を準備しても、位置を測るか、運動量を測るかによって得られる統計は異なります。

### 2.3 測定確率は内積の絶対値の二乗で決まる

状態 $${|\psi\rangle}$$ で物理量 $${\hat A}$$ を測定したとき、固有値 $${a}$$ を得る確率は、離散固有値の場合、

$$
P(a)=|\langle a|\psi\rangle|^2
$$

です。これをボルンの規則といいます。

測定を多数回繰り返したときの平均値、すなわち期待値は

$$
\langle\hat A\rangle
=
\langle\psi|\hat A|\psi\rangle
$$

で与えられます。

### 2.4 時間発展は確率を保存する

孤立した量子系の時間発展は、内積を保存するユニタリ演算子 $${\hat U(t)}$$ で表します。

$$
|\psi(t)\rangle=\hat U(t)|\psi(0)\rangle,
\qquad
\hat U^\dagger(t)\hat U(t)=1.
$$

したがって、

$$
\langle\psi(t)|\psi(t)\rangle
=
\langle\psi(0)|\psi(0)\rangle
$$

となり、全確率は時間がたっても $${1}$$ のままです。

---

## 3. 一個の粒子を記述するシュレーディンガー方程式

質量 $${m}$$ の一個の粒子がポテンシャル $${V(\mathbf x)}$$ の中を運動するとき、非相対論的量子力学の中心方程式は

$$
\boxed{
i\hbar\frac{\partial}{\partial t}\psi(\mathbf x,t)
=
\left(
-\frac{\hbar^2}{2m}\nabla^2+V(\mathbf x)
\right)\psi(\mathbf x,t)
}
$$

です。$${\psi(\mathbf x,t)}$$ は波動関数であり、

$$
|\psi(\mathbf x,t)|^2
$$

は時刻 $${t}$$ に位置 $${\mathbf x}$$ の近くで粒子を検出する確率密度です。

### 3.1 波動関数の状態空間

三次元空間全体で粒子を見つける確率は $${1}$$ なので、

$$
\int_{\mathbb R^3}|\psi(\mathbf x,t)|^2\,d^3x=1
$$

と正規化します。したがって一粒子の状態空間として、二乗積分可能な複素関数の空間

$$
\mathcal H_1=L^2(\mathbb R^3,d^3x)
$$

を用います。その内積は

$$
\langle\psi,\varphi\rangle
=
\int_{\mathbb R^3}
\psi(\mathbf x)^*\varphi(\mathbf x)\,d^3x
$$

です。

### 3.2 方程式を構成する

古典力学では、粒子のエネルギーと運動量に

$$
E=\frac{\mathbf p^2}{2m}+V(\mathbf x)
$$

という関係があります。一方、ド・ブロイの関係は、角振動数 $${\omega}$$、波数ベクトル $${\mathbf k}$$ とエネルギー、運動量を

$$
E=\hbar\omega,
\qquad
\mathbf p=\hbar\mathbf k
$$

で結びます。

平面波

$$
\psi(\mathbf x,t)
=
e^{i(\mathbf k\cdot\mathbf x-\omega t)}
$$

へ微分演算子を作用させると、

$$
i\hbar\frac{\partial\psi}{\partial t}
=
\hbar\omega\psi
=E\psi,
$$

$$
-i\hbar\nabla\psi
=
\hbar\mathbf k\psi
=\mathbf p\psi
$$

となります。そこでエネルギーと運動量に

$$
\hat E=i\hbar\frac{\partial}{\partial t},
\qquad
\hat{\mathbf p}=-i\hbar\nabla
$$

を対応させます。古典的なエネルギー関係へこの対応を適用すると、

$$
i\hbar\frac{\partial\psi}{\partial t}
=
\left(
\frac{(-i\hbar\nabla)^2}{2m}+V
\right)\psi
=
\left(
-\frac{\hbar^2}{2m}\nabla^2+V
\right)\psi
$$

を得ます。

これは数学的な定理だけから導いたものではなく、古典的なエネルギー関係、ド・ブロイの関係、線形な時間発展を同時に満たす方程式を構成する議論です。最終的な正当性は、この方程式の予測が実験と一致することによって確かめられます。

---

## 4. シュレーディンガー方程式は何を予測するのか

シュレーディンガー方程式へポテンシャルと境界条件を与えると、許される波動関数とエネルギーが決まります。ここでは、自由粒子、無限深井戸、有限障壁、調和振動子を順に計算します。

### 4.1 自由粒子――運動量が定まった波

一次元で $${V(x)=0}$$ とすると、

$$
i\hbar\frac{\partial\psi}{\partial t}
=
-\frac{\hbar^2}{2m}
\frac{\partial^2\psi}{\partial x^2}
$$

です。平面波

$$
\psi(x,t)=Ae^{i(kx-\omega t)}
$$

を代入します。左辺は

$$
i\hbar\frac{\partial\psi}{\partial t}
=
i\hbar(-i\omega)\psi
=
\hbar\omega\psi,
$$

右辺は

$$
-\frac{\hbar^2}{2m}
\frac{\partial^2\psi}{\partial x^2}
=
-\frac{\hbar^2}{2m}(ik)^2\psi
=
\frac{\hbar^2k^2}{2m}\psi
$$

です。したがって

$$
\hbar\omega
=
\frac{\hbar^2k^2}{2m}
$$

を得ます。$${E=\hbar\omega}$$、$${p=\hbar k}$$ を用いれば

$$
E=\frac{p^2}{2m}
$$

となり、自由粒子の古典的なエネルギー関係へ戻ります。

平面波は空間全体へ広がっていて正規化できないため、実際の局在した粒子は異なる $${k}$$ をもつ平面波の重ね合わせ、すなわち波束で表します。

### 4.2 無限深井戸――境界条件がエネルギーを離散化する

一次元で

$$
V(x)=
\begin{cases}
0 &(0<x<L),\\
\infty &(\text{それ以外})
\end{cases}
$$

というポテンシャルを考えます。粒子は $${0<x<L}$$ の外へ出られません。

時間と空間を分離して

$$
\psi(x,t)=\phi(x)e^{-iEt/\hbar}
$$

とおくと、井戸の内部で

$$
-\frac{\hbar^2}{2m}\frac{d^2\phi}{dx^2}
=E\phi
$$

となります。

$$
k^2:=\frac{2mE}{\hbar^2}
$$

と定義すれば、

$$
\frac{d^2\phi}{dx^2}+k^2\phi=0
$$

なので、一般解は

$$
\phi(x)=A\sin kx+B\cos kx
$$

です。

無限に高い壁では、両端で波動関数が消えなければなりません。

$$
\phi(0)=0,\qquad\phi(L)=0.
$$

最初の条件から $${B=0}$$、二つ目の条件から

$$
A\sin kL=0
$$

です。ゼロでない波動関数を求めているので $${A\neq0}$$ であり、

$$
\sin kL=0
\quad\Longrightarrow\quad
kL=n\pi,
\qquad n=1,2,3,\ldots
$$

となります。したがって

$$
k_n=\frac{n\pi}{L}
$$

だけが許され、エネルギーは

$$
\boxed{
E_n
=
\frac{\hbar^2k_n^2}{2m}
=
\frac{\hbar^2\pi^2n^2}{2mL^2}
}
$$

と離散化されます。

最後に正規化条件

$$
\int_0^L|\phi_n(x)|^2\,dx=1
$$

を課します。

$$
\int_0^L\sin^2\frac{n\pi x}{L}\,dx
=\frac L2
$$

なので、

$$
\boxed{
\phi_n(x)
=
\sqrt{\frac2L}
\sin\frac{n\pi x}{L}
}
$$

を得ます。

ここで重要なのは、エネルギーの離散性を最初から
仮定していないことです。微分方程式と境界条件を同時に満たす解を
求めた結果、許される $${k}$$ と $${E}$$ が離散化しました。

### 4.3 有限障壁――古典的に越えられない場所を透過する

次に

$$
V(x)=
\begin{cases}
V_0 &(0<x<L),\\
0 &(\text{それ以外})
\end{cases}
$$

という有限幅の障壁を考えます。粒子のエネルギーは $${E<V_0}$$ とします。

古典力学では障壁内の運動エネルギー $${E-V_0}$$ が負になるため、透過は不可能です。量子力学では各領域の定常解を

$$
\psi_{\mathrm I}(x)
=
e^{ikx}+re^{-ikx}
\qquad(x<0),
$$

$$
\psi_{\mathrm{II}}(x)
=
Ae^{\kappa x}+Be^{-\kappa x}
\qquad(0<x<L),
$$

$$
\psi_{\mathrm{III}}(x)
=
te^{ikx}
\qquad(x>L)
$$

と書けます。ここで

$$
k=\frac{\sqrt{2mE}}{\hbar},
\qquad
\kappa=\frac{\sqrt{2m(V_0-E)}}{\hbar}.
$$

$${r}$$ は反射振幅、$${t}$$ は透過振幅です。$${x=0,L}$$ で波動関数とその一階微分を連続にすると、

$$
1+r=A+B,
\qquad
ik(1-r)=\kappa(A-B),
$$

$$
Ae^{\kappa L}+Be^{-\kappa L}=te^{ikL},
$$

$$
\kappa\left(Ae^{\kappa L}-Be^{-\kappa L}\right)
=ikte^{ikL}
$$

を得ます。

後ろの二式から

$$
Ae^{\kappa L}
=
\frac{te^{ikL}}2
\left(1+\frac{ik}{\kappa}\right),
$$

$$
Be^{-\kappa L}
=
\frac{te^{ikL}}2
\left(1-\frac{ik}{\kappa}\right)
$$

です。これを最初の二式へ戻し、$${r}$$ を消去すると、

$$
t
=
\frac{2e^{-ikL}}
{2\cosh\kappa L
+i\left(\frac{\kappa}{k}-\frac{k}{\kappa}\right)
\sinh\kappa L}
$$

となります。透過係数 $${T}$$ は入射確率流に対する透過確率流の比です。この場合は左右で波数が同じなので、

$$
T=|t|^2
$$

です。よって

$$
\boxed{
T
=
\left[
1+
\frac{V_0^2}{4E(V_0-E)}
\sinh^2(\kappa L)
\right]^{-1}
}
$$

を得ます。

有限の $${L}$$ に対して右辺は正なので、

$$
E<V_0
\quad\text{でも}\quad
T>0
$$

です。障壁内で波動関数は指数関数的に減衰しますが、有限幅なら完全には消えません。これがトンネル効果です。

### 4.4 調和振動子――最低エネルギーはゼロにならない

ポテンシャル

$$
V(x)=\frac12m\omega^2x^2
$$

をもつ系を調和振動子といいます。ハミルトニアンは

$$
\hat H
=
\frac{\hat p^2}{2m}
+\frac12m\omega^2\hat x^2
$$

です。

位置表示では

$$
\hat x=x,
\qquad
\hat p=-i\hbar\frac d{dx}
$$

なので、任意の波動関数 $${\psi(x)}$$ に対して

$$
[\hat x,\hat p]\psi
=
x\left(-i\hbar\frac{d\psi}{dx}\right)
+i\hbar\frac d{dx}(x\psi)
=
i\hbar\psi.
$$

したがって

$$
[\hat x,\hat p]=i\hbar
$$

です。ここで $${[\hat A,\hat B]:=\hat A\hat B-\hat B\hat A}$$ を交換子といいます。

生成演算子 $${\hat a^\dagger}$$ と消滅演算子 $${\hat a}$$ を

$$
\hat a
=
\sqrt{\frac{m\omega}{2\hbar}}
\left(
\hat x+\frac{i}{m\omega}\hat p
\right),
$$

$$
\hat a^\dagger
=
\sqrt{\frac{m\omega}{2\hbar}}
\left(
\hat x-\frac{i}{m\omega}\hat p
\right)
$$

と定義します。先ほどの交換関係を用いると、

$$
[\hat a,\hat a^\dagger]=1
$$

です。また直接積を計算すると、

$$
\hat a^\dagger\hat a
=
\frac{m\omega}{2\hbar}\hat x^2
+\frac{1}{2m\hbar\omega}\hat p^2
-\frac12
$$

なので、

$$
\hat H
=
\hbar\omega
\left(
\hat a^\dagger\hat a+\frac12
\right)
$$

と書けます。

数演算子

$$
\hat N:=\hat a^\dagger\hat a
$$

を定義します。$${\hat N|n\rangle=n|n\rangle}$$ とすると、

$$
[\hat N,\hat a^\dagger]=\hat a^\dagger,
\qquad
[\hat N,\hat a]=-\hat a
$$

から、

$$
\hat N\hat a^\dagger|n\rangle
=(n+1)\hat a^\dagger|n\rangle,
$$

$$
\hat N\hat a|n\rangle
=(n-1)\hat a|n\rangle
$$

となります。$${\hat a^\dagger}$$ は固有値を一つ上げ、$${\hat a}$$ は一つ下げます。

一方、

$$
\langle n|\hat N|n\rangle
=
\|\hat a|n\rangle\|^2
\ge0
$$

なので、固有値は負になれません。降下操作はどこかで止まり、最低状態 $${|0\rangle}$$ は

$$
\hat a|0\rangle=0
$$

を満たします。そこから

$$
|n\rangle
\propto
(\hat a^\dagger)^n|0\rangle,
\qquad
n=0,1,2,\ldots
$$

が得られます。したがってエネルギー固有値は

$$
\boxed{
E_n
=
\hbar\omega
\left(n+\frac12\right)
}
$$

です。最低状態でも

$$
E_0=\frac12\hbar\omega
$$

が残ります。この零点エネルギーは、量子系を完全に静止させることができないという量子揺らぎの一例です。

---

## 5. 交換関係から不確定性原理が生まれる

位置 $${\hat x}$$ と運動量 $${\hat p}$$ は

$$
[\hat x,\hat p]=i\hbar
$$

を満たします。これは単なる計算規則ではありません。位置と運動量を同時にどこまで鋭く定められるかを制限します。

状態 $${|\psi\rangle}$$ における位置と運動量の期待値を

$$
\langle\hat x\rangle
=
\langle\psi|\hat x|\psi\rangle,
\qquad
\langle\hat p\rangle
=
\langle\psi|\hat p|\psi\rangle
$$

とします。平均からのずれを表す演算子を

$$
\delta\hat x:=\hat x-\langle\hat x\rangle,
\qquad
\delta\hat p:=\hat p-\langle\hat p\rangle
$$

と定義すると、標準偏差は

$$
(\Delta x)^2
=
\langle(\delta\hat x)^2\rangle,
\qquad
(\Delta p)^2
=
\langle(\delta\hat p)^2\rangle
$$

です。

二つのベクトル $${\delta\hat x|\psi\rangle}$$ と $${\delta\hat p|\psi\rangle}$$ へコーシー・シュワルツの不等式を適用すると、

$$
(\Delta x)^2(\Delta p)^2
\ge
\left|
\langle\delta\hat x\,\delta\hat p\rangle
\right|^2
$$

を得ます。任意の複素数 $${z}$$ に対して $${|z|\ge|\operatorname{Im}z|}$$ なので、

$$
\Delta x\,\Delta p
\ge
\left|
\operatorname{Im}
\langle\delta\hat x\,\delta\hat p\rangle
\right|.
$$

虚部は交換子を用いて

$$
\operatorname{Im}
\langle\delta\hat x\,\delta\hat p\rangle
=
\frac{1}{2i}
\langle[\delta\hat x,\delta\hat p]\rangle
$$

と書けます。定数は交換子へ寄与しないため、

$$
[\delta\hat x,\delta\hat p]
=[\hat x,\hat p]
=i\hbar
$$

です。よって

$$
\boxed{
\Delta x\,\Delta p
\ge
\frac{\hbar}{2}
}
$$

を得ます。

不確定性原理は、測定器の性能が悪いという主張ではありません。同じ量子状態を何度も準備して位置と運動量の統計を調べたとき、その二つの分布幅を同時に任意に小さくできないという、状態そのものへの制約です。

---

## 6. 同じ量子力学を別の描像で書く

ここまでは状態 $${|\psi(t)\rangle}$$ が時間発展し、演算子は原則として固定されるシュレーディンガー描像を用いました。同じ物理を、状態を固定し、演算子を時間発展させる形でも書けます。これをハイゼンベルク描像といいます。

ハミルトニアン $${\hat H}$$ が時間に依存しないとき、時間発展演算子は

$$
\hat U(t)
=
\exp\left(-\frac{i\hat Ht}{\hbar}\right)
$$

です。ハイゼンベルク描像の演算子を

$$
\hat A_H(t)
=
\hat U^\dagger(t)\hat A_S(t)\hat U(t)
$$

と定義します。添字 $${S}$$ はシュレーディンガー描像を表します。

この式を時間微分すると、

$$
\frac{d\hat A_H}{dt}
=
\frac{d\hat U^\dagger}{dt}\hat A_S\hat U
+\hat U^\dagger
\frac{\partial\hat A_S}{\partial t}
\hat U
+\hat U^\dagger\hat A_S
\frac{d\hat U}{dt}.
$$

ここで

$$
\frac{d\hat U}{dt}
=
-\frac{i}{\hbar}\hat H\hat U,
\qquad
\frac{d\hat U^\dagger}{dt}
=
\frac{i}{\hbar}\hat U^\dagger\hat H
$$

を代入すれば、

$$
\boxed{
\frac{d\hat A_H}{dt}
=
\frac{1}{i\hbar}
[\hat A_H,\hat H]
+\left(
\frac{\partial\hat A}{\partial t}
\right)_H
}
$$

を得ます。

シュレーディンガー描像とハイゼンベルク描像は、異なる実験予測を与える別理論ではありません。期待値

$$
\langle\psi_S(t)|\hat A_S|\psi_S(t)\rangle
=
\langle\psi_H|\hat A_H(t)|\psi_H\rangle
$$

が一致する、同じ量子力学の二つの表現です。

この演算子中心の見方は、空間の各点に演算子を割り当てる場の量子論へ進むときに有効になります。ただし、その前に特殊相対論との衝突を調べる必要があります。

---

## 7. 特殊相対論を課すと一粒子論が揺らぐ

非相対論的なシュレーディンガー方程式は時間について一階、空間について二階です。

$$
i\hbar\partial_t\psi
=
-\frac{\hbar^2}{2m}\nabla^2\psi+\cdots
$$

一方、特殊相対論では時間と空間をローレンツ変換で混ぜます。したがって、時間と空間を非対称に扱う方程式をそのまま基本方程式にはできません。

さらに相対論では、十分なエネルギーがあれば粒子・反粒子対を生成できます。粒子数を一個に固定する前提そのものが成り立たなくなります。

### 7.1 クライン・ゴルドン方程式

相対論的なエネルギーと運動量は

$$
E^2=c^2\mathbf p^2+m^2c^4
$$

を満たします。ここへ

$$
\hat E=i\hbar\partial_t,
\qquad
\hat{\mathbf p}=-i\hbar\nabla
$$

を代入すると、

$$
-\hbar^2\frac{\partial^2\phi}{\partial t^2}
=
\left(
-\hbar^2c^2\nabla^2+m^2c^4
\right)\phi
$$

です。整理すれば、

$$
\boxed{
\left(
\frac1{c^2}\frac{\partial^2}{\partial t^2}
-\nabla^2
+\frac{m^2c^2}{\hbar^2}
\right)\phi=0
}
$$

を得ます。これがクライン・ゴルドン方程式です。

平面波

$$
\phi(x)
=
e^{\frac{i}{\hbar}(\mathbf p\cdot\mathbf x-Et)}
$$

を代入すると、

$$
E=\pm\sqrt{c^2\mathbf p^2+m^2c^4}
$$

という正負二つの枝が現れます。

クライン・ゴルドン方程式からは、保存する密度 $${\rho}$$ と流れ $${\mathbf j}$$ を

$$
\rho
=
\frac{i\hbar}{2mc^2}
\left(
\phi^*\partial_t\phi
-(\partial_t\phi^*)\phi
\right),
$$

$$
\mathbf j
=
-\frac{i\hbar}{2m}
\left(
\phi^*\nabla\phi
-(\nabla\phi^*)\phi
\right)
$$

と作ることができ、

$$
\frac{\partial\rho}{\partial t}
+\nabla\cdot\mathbf j=0
$$

を満たします。平面波では

$$
\rho
=
\frac{E}{mc^2}|\phi|^2
$$

となるため、負エネルギー枝 $${E<0}$$ では $${\rho<0}$$ です。したがって、一般解全体に対して $${\rho}$$ を一粒子の確率密度と解釈することはできません。

自由理論の正の振動数部分だけから一粒子空間を構成すること自体はできます。
しかし、相互作用による粒子生成・消滅まで含めるには、
一粒子波動関数では不十分です。クライン・ゴルドン方程式は、
後にスピン $${0}$$ の場の運動方程式として解釈し直されます。

### 7.2 ディラック方程式

電子のようなスピン $${1/2}$$ の粒子については、時間と空間の両方に一階の方程式を作ることを考えます。ハミルトニアンを

$$
\hat H_D
=
c\boldsymbol\alpha\cdot\hat{\mathbf p}
+\beta mc^2
$$

と仮定します。ここで $${\alpha_i}$$ と $${\beta}$$ はまだ未知の係数です。

相対論的関係を再現するには、

$$
\hat H_D^2
=
c^2\hat{\mathbf p}^2+m^2c^4
$$

でなければなりません。左辺を展開すると、

$$
\hat H_D^2
=
c^2
\sum_{i,j}
\frac{\alpha_i\alpha_j+\alpha_j\alpha_i}{2}
\hat p_i\hat p_j
+mc^3
\sum_i
(\alpha_i\beta+\beta\alpha_i)\hat p_i
+\beta^2m^2c^4.
$$

不要な交差項を消し、各二乗項の係数を合わせるには、

$$
\{\alpha_i,\alpha_j\}=2\delta_{ij},
\qquad
\{\alpha_i,\beta\}=0,
\qquad
\alpha_i^2=\beta^2=1
$$

が必要です。ここで $${\{\hat A,\hat B\}:=\hat A\hat B+\hat B\hat A}$$ は反交換子です。

これらの条件は通常の数では満たせないため、$${\alpha_i,\beta}$$ は行列になります。最低次元は $${4}$$ であり、波動関数は四成分のスピノール

$$
\psi(x)
=
\begin{pmatrix}
\psi_1(x)\\
\psi_2(x)\\
\psi_3(x)\\
\psi_4(x)
\end{pmatrix}
$$

になります。

$$
\gamma^0:=\beta,
\qquad
\gamma^i:=\beta\alpha_i
$$

と定義すると、

$$
\{\gamma^\mu,\gamma^\nu\}
=
2\eta^{\mu\nu}
$$

です。$${\eta^{\mu\nu}=\operatorname{diag}(1,-1,-1,-1)}$$ はミンコフスキー計量です。方程式は

$$
\boxed{
\left(
i\hbar\gamma^\mu\partial_\mu-mc
\right)\psi=0
}
$$

と書けます。

この方程式は電子のスピンを記述しますが、やはり正負のエネルギー枝をもちます。場として量子化すると、二つの正エネルギー自由度は電子の二つのスピン状態に、負エネルギー枝に対応していた自由度は陽電子の二つのスピン状態に読み替えられます。

---

## 8. 固定粒子数から場の量子論へ

相対論的な反応では、

$$
\gamma+\gamma\longrightarrow e^-+e^+
$$

のように、二個の光子から電子と陽電子が生成されます。したがって、最初から「粒子は $${n}$$ 個」と固定した状態空間だけでは、反応の前後を同じ理論内で表せません。

### 8.1 固定された粒子数の状態空間

一粒子空間を $${\mathcal H_1}$$ とすると、区別可能な $${n}$$ 粒子の状態空間は

$$
\mathcal H_n
=
\mathcal H_1^{\otimes n}
$$

です。

同種粒子では粒子のラベルに物理的意味がありません。二粒子を交換する演算子を $${\hat P_{ij}}$$ とすると、交換を二回行えば元へ戻るので、

$$
\hat P_{ij}^2=1.
$$

交換によって物理状態が変わらず、全体位相だけが変わるなら、

$$
\hat P_{ij}|\Psi\rangle
=
\lambda|\Psi\rangle,
\qquad
|\lambda|=1.
$$

両式から

$$
\lambda^2=1
\quad\Longrightarrow\quad
\lambda=\pm1
$$

です。

- $${\lambda=+1}$$ の対称状態をとる粒子がボース粒子
- $${\lambda=-1}$$ の反対称状態をとる粒子がフェルミ粒子

です。したがって状態空間は

$$
\mathcal H_n^{\mathrm B}
=
\operatorname{Sym}^n\mathcal H_1,
\qquad
\mathcal H_n^{\mathrm F}
=
\bigwedge^n\mathcal H_1
$$

となります。

フェルミ粒子では、二粒子を同じ状態へ入れると

$$
\Psi(\ldots,x,\ldots,x,\ldots)
=
-\Psi(\ldots,x,\ldots,x,\ldots)
$$

なので、その波動関数は $${0}$$ です。これがパウリの排他原理です。

### 8.2 全粒子数を一つの空間へまとめる

粒子数が変わる理論では、

$$
\mathcal H
=
\mathcal H_0
\oplus\mathcal H_1
\oplus\mathcal H_2
\oplus\cdots
$$

と、すべての粒子数の空間を直和します。

一粒子空間を $${\mathfrak h}$$ とすると、ボース粒子とフェルミ粒子のフォック空間はそれぞれ

$$
\mathcal F_+(\mathfrak h)
=
\bigoplus_{n=0}^\infty
\operatorname{Sym}^n\mathfrak h,
$$

$$
\mathcal F_-(\mathfrak h)
=
\bigoplus_{n=0}^\infty
\bigwedge^n\mathfrak h
$$

です。$${\mathcal H_0}$$ に属する粒子数ゼロの状態を真空 $${|0\rangle}$$ といいます。

### 8.3 場を量子化する

最も単純な実スカラー場 $${\phi(x)}$$ を考えます。以下では式を見やすくするため、自然単位系 $${c=\hbar=1}$$ を使います。

古典場のラグランジアン密度を

$$
\mathcal L
=
\frac12\partial_\mu\phi\,\partial^\mu\phi
-\frac12m^2\phi^2
$$

とします。作用

$$
S=\int d^4x\,\mathcal L
$$

を停留させるオイラー・ラグランジュ方程式から、

$$
(\partial_\mu\partial^\mu+m^2)\phi=0
$$

を得ます。これはクライン・ゴルドン方程式です。ここでは一粒子の波動方程式ではなく、古典場の運動方程式として現れています。

共役運動量場を

$$
\pi(\mathbf x,t)
:=
\frac{\partial\mathcal L}{\partial\dot\phi}
=
\dot\phi
$$

と定義します。量子化では $${\phi,\pi}$$ を演算子値の場 $${\hat\phi,\hat\pi}$$ に置き換え、同時刻交換関係

$$
\boxed{
[\hat\phi(\mathbf x,t),\hat\pi(\mathbf y,t)]
=
i\delta^{(3)}(\mathbf x-\mathbf y)
}
$$

を課します。これは一粒子量子力学の $${[\hat x,\hat p]=i}$$ を、空間の各点に自由度をもつ系へ拡張した式です。

### 8.4 粒子は場の励起として現れる

自由スカラー場は

$$
\hat\phi(x)
=
\int
\frac{d^3p}{(2\pi)^3}
\frac1{\sqrt{2E_{\mathbf p}}}
\left(
\hat a_{\mathbf p}e^{-ip\cdot x}
+\hat a_{\mathbf p}^\dagger e^{ip\cdot x}
\right),
$$

$$
E_{\mathbf p}
=
\sqrt{\mathbf p^2+m^2}
$$

とモード展開できます。

$${\hat a_{\mathbf p}^\dagger}$$ は運動量 $${\mathbf p}$$ の量子を
一個作る生成演算子、$${\hat a_{\mathbf p}}$$ は一個消す消滅演算子です。

$$
[\hat a_{\mathbf p},\hat a_{\mathbf q}^\dagger]
=
(2\pi)^3\delta^{(3)}(\mathbf p-\mathbf q)
$$

を満たし、真空は

$$
\hat a_{\mathbf p}|0\rangle=0
$$

で定義されます。したがって、

$$
|\mathbf p\rangle
=
\hat a_{\mathbf p}^\dagger|0\rangle
$$

が一粒子状態、

$$
|\mathbf p,\mathbf q\rangle
=
\hat a_{\mathbf p}^\dagger
\hat a_{\mathbf q}^\dagger
|0\rangle
$$

が二粒子状態です。

ここで見方が逆転しています。場の量子論では、粒子を最初から基本的な小球として置くのではありません。**場が基本変数であり、粒子は場の一つのモードが離散的に励起された状態として現れます。**

フェルミ粒子である電子の場には交換関係ではなく反交換関係

$$
\{
\hat\psi_\alpha(\mathbf x,t),
\hat\psi_\beta^\dagger(\mathbf y,t)
\}
=
\delta_{\alpha\beta}
\delta^{(3)}(\mathbf x-\mathbf y)
$$

を課します。これにより、同じ一粒子状態を二個の電子が占められないことが代数そのものへ組み込まれます。

---

## 9. 対称性から電磁相互作用を作る

電子・陽電子と光子を記述する理論が量子電磁気学、Quantum Electrodynamics（QED）です。その中心方程式はラグランジアン密度

$$
\boxed{
\mathcal L_{\mathrm{QED}}
=
\bar\psi(i\gamma^\mu D_\mu-m)\psi
-\frac14F_{\mu\nu}F^{\mu\nu}
}
$$

です。ここでも自然単位系 $${c=\hbar=1}$$ を用います。

この式を最初から仮定するのではなく、自由な電子場へ局所的な位相対称性を要求することで構成します。

### 9.1 自由な電子場

自由なディラック場のラグランジアン密度は

$$
\mathcal L_{\mathrm D}
=
\bar\psi(i\gamma^\mu\partial_\mu-m)\psi
$$

です。ここで

$$
\bar\psi:=\psi^\dagger\gamma^0
$$

をディラック共役といいます。

全時空点で同じ定数 $${\alpha}$$ を用いる位相変換

$$
\psi(x)\longmapsto e^{-i\alpha}\psi(x)
$$

の下で、$${\mathcal L_{\mathrm D}}$$ は不変です。この大域的な $${U(1)}$$ 対称性にネーターの定理を適用すると、

$$
j^\mu=\bar\psi\gamma^\mu\psi,
\qquad
\partial_\mu j^\mu=0
$$

という保存電流を得ます。これは電荷保存に対応します。

### 9.2 位相を時空点ごとに変える

次に、位相を時空点ごとに選び直す

$$
\psi(x)
\longmapsto
e^{-i\alpha(x)}\psi(x)
$$

という局所変換を考えます。通常の微分は

$$
\partial_\mu\psi
\longmapsto
e^{-i\alpha(x)}
\left[
\partial_\mu\psi
-i(\partial_\mu\alpha)\psi
\right]
$$

となり、$${\partial_\mu\alpha}$$ を含む余分な項が現れます。このままでは自由ラグランジアンは不変ではありません。

そこで電磁ポテンシャル $${A_\mu}$$ を導入し、共変微分を

$$
D_\mu:=\partial_\mu+ieA_\mu
$$

と定義します。同時に

$$
A_\mu
\longmapsto
A_\mu+\frac1e\partial_\mu\alpha
$$

と変換させると、

$$
D_\mu\psi
\longmapsto
e^{-i\alpha(x)}D_\mu\psi
$$

となります。$${D_\mu\psi}$$ は $${\psi}$$ と同じ仕方で変換するため、

$$
\bar\psi i\gamma^\mu D_\mu\psi
$$

は局所変換の下で不変です。

電磁場の強さを

$$
F_{\mu\nu}
:=
\partial_\mu A_\nu-\partial_\nu A_\mu
$$

と定義すると、$${F_{\mu\nu}}$$ も局所変換の下で不変です。したがって、ローレンツ不変で微分の次数が低いラグランジアンとして

$$
\mathcal L_{\mathrm{QED}}
=
\bar\psi(i\gamma^\mu D_\mu-m)\psi
-\frac14F_{\mu\nu}F^{\mu\nu}
$$

を得ます。

共変微分を展開すると、

$$
\mathcal L_{\mathrm{QED}}
=
\bar\psi(i\gamma^\mu\partial_\mu-m)\psi
-\frac14F_{\mu\nu}F^{\mu\nu}
-e\bar\psi\gamma^\mu A_\mu\psi.
$$

最後の

$$
\boxed{
\mathcal L_{\mathrm{int}}
=
-e\bar\psi\gamma^\mu A_\mu\psi
=
-ej^\mu A_\mu
}
$$

が、電子場と電磁場の相互作用です。

局所対称性だけがどのような理論も一意に決めるわけではありません。
ここでは場の種類、ローレンツ不変性、局所性、
微分の次数が低い最小結合という条件も使っています。
その条件の下で、局所 $${U(1)}$$ 対称性が相互作用の形を強く制約します。

### 9.3 量子化すると光子の放出・吸収になる

場を量子化すると、$${\psi}$$ の量子が電子・陽電子、$${A_\mu}$$ の量子が光子です。したがって

$$
-e\bar\psi\gamma^\mu A_\mu\psi
$$

は、電子や陽電子が光子を放出・吸収する過程を表します。電子同士の電磁相互作用は、摂動論では光子を交換する過程として計算されます。

つまりQEDは、「電子の間に力が働く」という記述を、**電子場と電磁場の局所的な相互作用**へ置き換えた理論です。

---

## 10. 繰り込みは何をしているのか

QEDで相互作用を摂動展開すると、途中で仮想的な電子・陽電子・光子が現れて消えるループ過程が含まれます。その運動量をすべて積分すると、高運動量領域で発散が現れます。

たとえば電子の自己エネルギーには、模式的に

$$
\Sigma(p)
\sim
e^2
\int\frac{d^4k}{(2\pi)^4}
\gamma^\mu
\frac{\gamma^\rho(p-k)_\rho+m}
{(p-k)^2-m^2}
\gamma_\mu
\frac1{k^2}
$$

のような積分が現れます。$${p}$$ は外部の電子の運動量、$${k}$$ はループ内の仮想光子の運動量です。$${|k|\to\infty}$$ の寄与まで素朴に積分すると発散します。

繰り込みでは、ラグランジアンに最初に書いた裸の場・質量・電荷を

$$
\psi_0=Z_2^{1/2}\psi,
\qquad
A_{0\mu}=Z_3^{1/2}A_\mu,
$$

$$
m_0=m+\delta m,
\qquad
e_0=Z_e e
$$

と書き換えます。するとラグランジアンは

$$
\mathcal L(m_0,e_0,\psi_0,A_0)
=
\mathcal L_{\mathrm{ren}}(m,e,\psi,A)
+\mathcal L_{\mathrm{ct}}
$$

に分かれます。$${\mathcal L_{\mathrm{ct}}}$$ は反項であり、ループ積分の発散を打ち消します。

重要なのは、反項の有限部分を勝手に決めるのではなく、測定条件で固定することです。

- 質量 $${m}$$ は、電子の伝播関数の極が測定された電子質量に対応する位置へ来るように定義する
- 電荷 $${e}$$ は、指定したエネルギー尺度で測定される電磁相互作用の強さとして定義する

この手続きにより、有限個の測定値を入力として、別の観測量を有限な値として予測できます。

結合定数は、定義するエネルギー尺度 $${\mu}$$ に依存します。

$$
\mu\frac{de}{d\mu}
=
\beta(e).
$$

一種類の荷電ディラック場をもつQEDでは、最低次で

$$
\beta(e)
=
\frac{e^3}{12\pi^2}+\cdots
$$

です。これは電子の電荷が時間とともに変化するという意味ではありません。異なる距離尺度で真空の分極をどこまで分解して観測するかによって、有効な相互作用の強さが変わるという意味です。

繰り込みは、無限大を隠すだけの技巧ではありません。測定される量を基準に理論のパラメータを定め、観測する尺度に応じた有効な記述を作る手続きです。

---

## 11. 一般のゲージ理論と標準模型

QEDの局所 $${U(1)}$$ 対称性は、内部自由度を複数成分へ拡張できます。

内部対称性の生成子を $${T^a}$$ とし、

$$
[T^a,T^b]
=
if^{abc}T^c
$$

とします。$${f^{abc}}$$ は構造定数です。共変微分を

$$
D_\mu
=
\partial_\mu+igA_\mu^aT^a
$$

と定義すると、場の強さは

$$
[D_\mu,D_\nu]
=
igF_{\mu\nu}^aT^a
$$

から求まり、

$$
F_{\mu\nu}^a
=
\partial_\mu A_\nu^a
-\partial_\nu A_\mu^a
-gf^{abc}A_\mu^bA_\nu^c
$$

となります。

$${U(1)}$$ では生成子が実質的に一つで $${f^{abc}=0}$$ なので、最後の項はありません。一方、生成子同士が交換しない非可換ゲージ理論では最後の項が残り、ゲージ場同士が直接相互作用します。

標準模型のゲージ群は

$$
\boxed{
G_{\mathrm{SM}}
=
SU(3)_c
\times
SU(2)_L
\times
U(1)_Y
}
$$

です。

### 11.1 強い相互作用

$${SU(3)_c}$$ はクォークの三種類の色自由度に作用します。「色」は実際の色ではなく、三成分の内部自由度の名称です。対応する八種類のゲージ場がグルーオンです。

$$
D_\mu q
=
\left(
\partial_\mu+ig_sG_\mu^aT^a
\right)q.
$$

$${SU(3)}$$ は非可換なので、グルーオン自身も色の荷をもち、グルーオン同士が相互作用します。

### 11.2 弱い相互作用と電磁相互作用

電弱理論のゲージ群は

$$
SU(2)_L\times U(1)_Y
$$

です。左巻きの電子とニュートリノは

$$
L
=
\begin{pmatrix}
\nu_e\\
e
\end{pmatrix}_L
$$

という $${SU(2)_L}$$ 二重項を作ります。一方、右巻き電子は $${SU(2)_L}$$ 一重項です。この左右非対称な構造が、弱い相互作用における空間反転対称性の破れと結びついています。

電荷は

$$
Q=T_3+Y
$$

で与えられます。ここではこの式になるようにハイパーチャージ $${Y}$$ を規格化しています。

### 11.3 ヒッグス場と質量

ゲージ対称性を保ったままでは、弱い相互作用の媒介粒子へ質量項を直接加えられません。そこで複素二重項のヒッグス場

$$
\Phi
=
\begin{pmatrix}
\phi^+\\
\phi^0
\end{pmatrix}
$$

とポテンシャル

$$
V(\Phi)
=
-\mu^2\Phi^\dagger\Phi
+\lambda(\Phi^\dagger\Phi)^2,
\qquad
\mu^2>0,\ \lambda>0
$$

を導入します。

真空でヒッグス場が

$$
\langle\Phi\rangle
=
\frac1{\sqrt2}
\begin{pmatrix}
0\\
v
\end{pmatrix}
$$

という値をとると、

$$
SU(2)_L\times U(1)_Y
\longrightarrow
U(1)_{\mathrm{em}}
$$

という形で、真空が保つ対称性が小さくなります。その結果、

$$
M_W=\frac12gv,
\qquad
M_Z=\frac12\sqrt{g^2+g'^2}\,v
$$

となり、$${W^\pm}$$ と $${Z}$$ は質量をもちます。一方、破れずに残った $${U(1)_{\mathrm{em}}}$$ に対応する光子は質量ゼロのままです。

---

## 12. 離散対称性はすべて保存されるわけではない

連続的なゲージ対称性とは別に、場の量子論では次の離散変換も調べます。

$$
C:\text{粒子}\leftrightarrow\text{反粒子},
$$

$$
P:(t,\mathbf x)\longmapsto(t,-\mathbf x),
$$

$$
T:(t,\mathbf x)\longmapsto(-t,\mathbf x).
$$

$${C}$$ は電荷反転、$${P}$$ は空間反転、$${T}$$ は時間反転です。

電磁相互作用と強い相互作用は、通常の条件では $${C}$$ や $${P}$$ を
よい対称性として扱えます。一方、弱い相互作用は左巻き成分と
右巻き成分を異なる仕方で扱うため、$${P}$$ を破ります。
さらに弱い相互作用では、粒子・反粒子の入れ替えと空間反転を
組み合わせた $${CP}$$ もわずかに破れます。

それでも、局所性、ローレンツ不変性、ユニタリ性、安定な真空などの標準的な前提を満たす量子場理論では、三つをすべて組み合わせた $${CPT}$$ が保存されます。これをCPT定理といいます。

CPT対称性からは、粒子と反粒子の質量が等しいことなどが従います。もしCPTの破れが確立すれば、個別の相互作用だけでなく、局所相対論的量子場理論の前提そのものを再検討する必要があります。

---

## 13. 量子論の全体像

量子論の発展を、解決した問題と数式の対応でまとめます。

### 古典物理学の限界

黒体放射、光電効果、原子スペクトルは、エネルギー交換と原子の状態を連続量だけで記述できないことを示しました。

$$
E=h\nu,
\qquad
h\nu=E_n-E_m.
$$

### 非相対論的量子力学

状態を複素ベクトル、物理量を自己共役演算子として表し、ボルンの規則で測定確率を与えます。一粒子の時間発展はシュレーディンガー方程式で決まります。

$$
i\hbar\partial_t\psi
=
\left(
-\frac{\hbar^2}{2m}\nabla^2+V
\right)\psi.
$$

境界条件を課すと、許される状態とエネルギーが離散化します。非可換な物理量には、同時に鋭い値をもてない制約があります。

$$
[\hat x,\hat p]=i\hbar,
\qquad
\Delta x\,\Delta p\ge\frac{\hbar}{2}.
$$

### 相対論的量子論

特殊相対論と両立する一階方程式を求めると、波動関数はスピノールになり、ディラック方程式が得られます。

$$
(i\hbar\gamma^\mu\partial_\mu-mc)\psi=0.
$$

しかし正負のエネルギー枝と粒子対生成は、固定粒子数の一粒子論では十分に扱えません。

### 場の量子論

状態空間をすべての粒子数の直和であるフォック空間へ広げ、場を演算子として量子化します。

$$
\mathcal F_\pm(\mathfrak h)
=
\bigoplus_{n=0}^\infty
\begin{cases}
\operatorname{Sym}^n\mathfrak h &(\text{ボース粒子}),\\
\bigwedge^n\mathfrak h &(\text{フェルミ粒子}).
\end{cases}
$$

粒子は場の離散的な励起であり、生成・消滅演算子が異なる粒子数の状態を結びます。

### 相互作用と標準模型

局所ゲージ対称性は、物質場とゲージ場の結合を制約します。QEDでは

$$
D_\mu=\partial_\mu+ieA_\mu
$$

から電子・陽電子と光子の相互作用が現れます。この考えを非可換な内部対称性へ拡張したものが、標準模型の

$$
SU(3)_c\times SU(2)_L\times U(1)_Y
$$

です。

量子論が最終的に変えたのは、粒子の軌道を計算する公式だけではありません。

> 物理系の状態は確率振幅で表され、観測量は演算子として作用する。相対論的な世界では場が基本変数となり、粒子はその場の量子的な励起として現れる。

これが、シュレーディンガー方程式から場の量子論までを貫く一本の流れです。
