---
marp: true
size: 16:9
theme: am_blue
paginate: true
headingDivider: [2,3]
math: katex
footer: \ *Supplemental Topic* *Legendre Transform and Thermodynamic Potentials*
---

<!-- _class: cover_e -->
<!-- _paginate: "" -->
<!-- _footer: ![](../example_images/logo.png) -->
<!-- _header: ![](../example_images/logo_1.png) -->

# <!-- fit -->Legendre Transform

###### <br> for thermodynamics and statistical physics

From natural variables to useful potentials  
Prepared in English with Awesome Marp

---

<!-- _class: toc_a -->
<!-- _header: "CONTENTS" -->
<!-- _footer: "" -->
<!-- _paginate: "" -->

- [Why Legendre transforms appear in thermodynamics](#3)
- [The mathematical construction](#5)
- [Conjugate pairs and thermodynamic potentials](#8)
- [Chemical potential and multi-component systems](#13)
- [Another example: electric work](#16)
- [Key takeaways](#18)

## Why Legendre transforms appear in thermodynamics

<!-- _class: trans -->
<!-- _footer: "" -->
<!-- _paginate: "" -->

## Why do we need a new potential?

<!-- _class: navbar -->
<!-- _header: \ ***Legendre Transform*** **Motivation** *Math Setup* *Potentials* *Chemical Potential* *Electric Work* *Takeaways* -->

- A thermodynamic function is most useful when its natural variables are the quantities we can control in the lab.
- But the internal energy is written as $U=U(S,V,N)$, while experiments often fix $T$, $P$, or $\mu$ instead.
- The Legendre transform exchanges an extensive variable for its intensive conjugate.
- This gives new potentials with simpler differentials and direct physical criteria for equilibrium.

> #### Main idea
>
> Replace a slope-controlled description by an intercept-like description.

## A geometric preview

<!-- _class: navbar cols-2 -->
<!-- _header: \ ***Legendre Transform*** **Motivation** *Math Setup* *Potentials* *Chemical Potential* *Electric Work* *Takeaways* -->

<div class=ldiv>

- For a convex function $f(x)$, define its slope
  $$p=\frac{df}{dx}.$$
- The tangent line at $x$ is
  $$y=px-\big(px-f(x)\big).$$
- The quantity
  $$g(p)=px-f(x)$$
  depends on the slope rather than on the original coordinate.

</div>
<div class=rdiv>

> #### Interpretation
>
> - $x$ is the original variable
> - $p$ is the conjugate variable
> - $g(p)$ stores the same information in a new coordinate system

For convex $f$, the map between $x$ and $p$ is one-to-one, so the transform is reversible.

</div>

## The mathematical construction

<!-- _class: trans -->
<!-- _footer: "" -->
<!-- _paginate: "" -->

## Legendre transform in one variable

<!-- _class: navbar -->
<!-- _header: \ *Legendre Transform* *Motivation* **Math Setup** *Potentials* *Chemical Potential* *Electric Work* *Takeaways* -->

Given a differentiable convex function $f(x)$,

$$
p=\frac{df}{dx}, \qquad g(p)=px-f(x).
$$

Then

$$
\frac{dg}{dp}=x.
$$

- The new independent variable is $p$ instead of $x$.
- The transform subtracts the term needed to remove $dx$ from the differential.
- In thermodynamics, this is exactly how we move from $U$ to $F$, $H$, $G$, or $\Omega$.

## Differential viewpoint: the thermodynamic version

<!-- _class: navbar cols-2 -->
<!-- _header: \ *Legendre Transform* *Motivation* **Math Setup** *Potentials* *Chemical Potential* *Electric Work* *Takeaways* -->

<div class=ldiv>

Start from the fundamental relation for a simple system:

$$
dU = T\,dS - P\,dV + \mu\,dN.
$$

So the conjugate pairs are

- $T \leftrightarrow S$
- $-P \leftrightarrow V$
- $\mu \leftrightarrow N$

</div>
<div class=rdiv>

If we want to replace $S$ by $T$, define

$$
F=U-TS.
$$

Then

$$
dF = -S\,dT - P\,dV + \mu\,dN.
$$

Now $F$ has natural variables $(T,V,N)$.

</div>

## Conjugate pairs and sign conventions

<!-- _class: navbar -->
<!-- _header: \ *Legendre Transform* *Motivation* **Math Setup** *Potentials* *Chemical Potential* *Electric Work* *Takeaways* -->

| General form | Thermodynamic meaning |
|---|---|
| $dU = T\,dS - P\,dV + \mu\,dN$ | fundamental differential |
| $T=\left(\partial U/\partial S\right)_{V,N}$ | conjugate to entropy |
| $-P=\left(\partial U/\partial V\right)_{S,N}$ | conjugate to volume |
| $\mu=\left(\partial U/\partial N\right)_{S,V}$ | conjugate to particle number |

The minus sign for pressure comes from mechanical work $\delta W = P\,dV$, so $dU = \delta Q - \delta W$ gives $-P\,dV$.

## Thermodynamic potentials from Legendre transforms

<!-- _class: trans -->
<!-- _footer: "" -->
<!-- _paginate: "" -->

## The standard family of potentials

<!-- _class: navbar -->
<!-- _header: \ *Legendre Transform* *Motivation* *Math Setup* **Potentials** *Chemical Potential* *Electric Work* *Takeaways* -->

| Potential | Definition | Natural variables |
|---|---|---|
| Internal energy $U$ | $U$ | $(S,V,N)$ |
| Helmholtz free energy $F$ | $U-TS$ | $(T,V,N)$ |
| Enthalpy $H$ | $U+PV$ | $(S,P,N)$ |
| Gibbs free energy $G$ | $U-TS+PV$ | $(T,P,N)$ |
| Grand potential $\Omega$ | $U-TS-\mu N$ | $(T,V,\mu)$ |

Each new potential is chosen to match a common experimental control set.

## Reading conjugate pairs from differentials

<!-- _class: navbar cols-2 -->
<!-- _header: \ *Legendre Transform* *Motivation* *Math Setup* **Potentials** *Chemical Potential* *Electric Work* *Takeaways* -->

<div class=ldiv>

$$
\begin{aligned}
dF &= -S\,dT - P\,dV + \mu\,dN,\\
dH &= T\,dS + V\,dP + \mu\,dN,\\
dG &= -S\,dT + V\,dP + \mu\,dN.
\end{aligned}
$$

</div>
<div class=rdiv>

This immediately gives

$$
S=-\left(\frac{\partial F}{\partial T}\right)_{V,N},\qquad
P=-\left(\frac{\partial F}{\partial V}\right)_{T,N},
$$

and similarly for $H$ and $G$.

> Useful rule: the coefficient of a differential is the conjugate variable.

</div>

## A compact map of Legendre moves

<!-- _class: navbar bq-blue -->
<!-- _header: \ *Legendre Transform* *Motivation* *Math Setup* **Potentials** *Chemical Potential* *Electric Work* *Takeaways* -->

> #### Starting from $U(S,V,N)$
>
> - transform in $S$ $\rightarrow$ $F(T,V,N)=U-TS$
> - transform in $V$ $\rightarrow$ $H(S,P,N)=U+PV$
> - transform in $S$ and $V$ $\rightarrow$ $G(T,P,N)=U-TS+PV$
> - transform in $S$ and $N$ $\rightarrow$ $\Omega(T,V,\mu)=U-TS-\mu N$

Legendre transforms can be done one variable at a time or several at once.

## Chemical potential and multi-component systems

<!-- _class: trans -->
<!-- _footer: "" -->
<!-- _paginate: "" -->

## What is chemical potential?

<!-- _class: navbar -->
<!-- _header: \ *Legendre Transform* *Motivation* *Math Setup* *Potentials* **Chemical Potential** *Electric Work* *Takeaways* -->

For a one-component system,

$$
\mu = \left(\frac{\partial U}{\partial N}\right)_{S,V}
= \left(\frac{\partial G}{\partial N}\right)_{T,P}.
$$

- It is the energy cost of adding one particle while holding the specified variables fixed.
- It controls particle exchange, just as temperature controls entropy exchange and pressure controls volume exchange.
- Its conjugate extensive variable is the particle number $N$.

## Multi-component systems

<!-- _class: navbar cols-2 -->
<!-- _header: \ *Legendre Transform* *Motivation* *Math Setup* *Potentials* **Chemical Potential** *Electric Work* *Takeaways* -->

<div class=ldiv>

For several species,

$$
dU = T\,dS - P\,dV + \sum_i \mu_i\, dN_i.
$$

and therefore

$$
dG = -S\,dT + V\,dP + \sum_i \mu_i\, dN_i.
$$

</div>
<div class=rdiv>

- Each species has its own chemical potential $\mu_i$.
- Diffusion and chemical reaction are driven by differences in chemical potential.
- In equilibrium at fixed $T$ and $P$, matter redistributes until the appropriate $\mu_i$ balances are satisfied.

</div>

## Why the grand canonical ensemble uses $\mu$

<!-- _class: navbar -->
<!-- _header: \ *Legendre Transform* *Motivation* *Math Setup* *Potentials* **Chemical Potential** *Electric Work* *Takeaways* -->

- In statistical mechanics, a system in contact with a heat and particle reservoir has fixed $T$, $V$, and $\mu$.
- The matching thermodynamic potential is the grand potential
  $$
  \Omega = U - TS - \mu N = F - \mu N.
  $$
- Its differential is
  $$
  d\Omega = -S\,dT - P\,dV - N\,d\mu.
  $$
- This is the ensemble-level version of the same Legendre-transform logic.

## Another example: electric work

<!-- _class: trans -->
<!-- _footer: "" -->
<!-- _paginate: "" -->

## Electric potential and charge

<!-- _class: navbar cols-2 -->
<!-- _header: \ *Legendre Transform* *Motivation* *Math Setup* *Potentials* *Chemical Potential* **Electric Work** *Takeaways* -->

<div class=ldiv>

Suppose a system can also exchange charge $Q$.

An electric-work contribution may appear as

$$
dU = T\,dS - P\,dV + \mu\,dN + \Phi\,dQ,
$$

where $\Phi$ is electric potential.

</div>
<div class=rdiv>

Then $\Phi$ and $Q$ are another conjugate pair.

If $\Phi$ is externally controlled, define

$$
\widetilde U = U - \Phi Q.
$$

Its differential contains $-Q\,d\Phi$, so the natural variable becomes $\Phi$ instead of $Q$.

</div>

## Takeaways

<!-- _class: trans -->
<!-- _footer: "" -->
<!-- _paginate: "" -->

## The main message

<!-- _class: navbar bq-green -->
<!-- _header: \ *Legendre Transform* *Motivation* *Math Setup* *Potentials* *Chemical Potential* *Electric Work* **Takeaways** -->

> #### Remember these points
>
> - A Legendre transform replaces a variable by its conjugate slope.
> - In thermodynamics, it converts $U(S,V,N)$ into potentials adapted to fixed $T$, $P$, or $\mu$.
> - Known conjugate pairs include $(T,S)$, $(P,V)$ with the thermodynamic sign convention, and $(\mu,N)$.
> - Chemical potential is the variable conjugate to particle number and becomes central for multi-component systems and the grand canonical ensemble.
> - The same logic also applies beyond mechanical work, for example to electric potential and charge.

## Thank you

<!-- _class: cover_b -->
<!-- _header: "" -->
<!-- _footer: "" -->
<!-- _paginate: "" -->

# Questions?

### Legendre transforms connect mathematics, thermodynamics, and statistical physics.
