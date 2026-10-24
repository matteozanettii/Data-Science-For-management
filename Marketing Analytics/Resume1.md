# Customer Analytics: Formula Cheat Sheet & Self-Assessment Quiz

## 📊 1. FORMULA CHEAT SHEET

| Metric | Short Meaning | Formula / Calculation |
| :--- | :--- | :--- |
| **Acquisition Rate** | Rate of new prospects acquired | `(Prospects acquired / Prospects targeted) * 100` |
| **Acquisition Cost (CAC)** | Cost to acquire a new customer | `Acquisition spending / # of prospects acquired` |
| **Retention Rate** | Rate of customers who stay | `(# customers buying in t / # customers buying in t-1) * 100` |
| **Defection / Churn Rate** | Rate of customers who leave | `(# customers NOT buying in t / # customers buying in t-1) * 100` |
| **Survival Rate** | Customers from the initial cohort still active | `(# customers from initial period still active in t / Initial total # of customers) * 100` |
| **Average Inter-purchase Time** | Average days between purchases | `(Sum of days between purchases) / (Number of intervals)` |
| **Periodicity** | How regular the customer is (Standard Deviation) | `Standard Deviation of inter-purchase times` |
| **Recency** | Days since the *last* purchase | `Date of analysis - Date of last purchase` |
| **Frequency** | Total number of purchases | `Total count of purchases` |
| **Redemption Rate (Coupon)** | Coupon redemption rate | `(# coupons redeemed / Total # coupons issued) * 100` |
| **Redemption Rate (Loyalty)** | Points redemption rate | `(# points spent on rewards / Total # points issued) * 100` |
| **Net Promoter Score (NPS)** | Customer recommendation index | `% Promoters (9-10) - % Detractors (0-6)` |

---

## 📝 2. SELF-ASSESSMENT QUIZ

### 🟢 Section 1: Formulas (Write the exact formula)

**1.** How do you calculate the **Acquisition Cost (CAC)**?
<details>
<summary>👉 Show answer</summary>
<b>Formula:</b> Acquisition spending / # of prospects acquired
</details>

**2.** How do you calculate the **Retention Rate** for a cohort?
<details>
<summary>👉 Show answer</summary>
<b>Formula:</b> (# of customers in the segment buying in t / Total # of customers in the segment buying in t-1) * 100
</details>

**3.** How do you calculate the **Redemption Rate** for coupons?
<details>
<summary>👉 Show answer</summary>
<b>Formula:</b> (Number of coupons redeemed / Total number of coupons issued) * 100
</details>

**4.** Write the formula for the **Net Promoter Score (NPS)**.
<details>
<summary>👉 Show answer</summary>
<b>Formula:</b> % Promoters - % Detractors
<br><i>(Note: Passives are never included in the formula!)</i>
</details>

<br>

### 🟡 Section 2: True or False

**5.** **Recency** measures the total number of times a customer has made a purchase.
<details>
<summary>👉 Show answer</summary>
<b>FALSE.</b> Recency measures the days since the <b>last</b> purchase. The total number of purchases is <b>Frequency</b>.
</details>

**6.** **Periodicity** is the standard deviation of inter-purchase times. If its value is very low, it means the customer is very regular and predictable in their purchases.
<details>
<summary>👉 Show answer</summary>
<b>TRUE.</b> A low standard deviation indicates that the days between purchases are always very similar (e.g., buying every 15 days). A high value indicates irregular behavior.
</details>

**7.** **Survival Rate** is always calculated by taking the previous year (t-1) as a reference.
<details>
<summary>👉 Show answer</summary>
<b>FALSE.</b> That is the Retention Rate. <b>Survival Rate</b> always takes the <b>initial period (period 0)</b> as a reference and measures how many of those original customers are still active at time t.
</details>

**8.** Retention Rate + Defection (Churn) Rate = 100%.
<details>
<summary>👉 Show answer</summary>
<b>TRUE.</b> They are two sides of the same coin: those who are not "retained" necessarily "churn".
</details>

<br>

### 🔴 Section 3: Comprehension and Logic

**9.** If a manager asks you to calculate the **Average Inter-purchase Time** of a customer, what exactly are you calculating?
<details>
<summary>👉 Show answer</summary>
The mathematical <b>average</b> of the days elapsed between one purchase and the next. (E.g., If the intervals between their purchases were 10 days, 14 days, and 12 days, the average is 12 days).
</details>

**10.** A customer has a high **Recency**. Are they a good customer or a customer at risk?
<details>
<summary>👉 Show answer</summary>
They are a <b>customer at risk (churner)</b>. High Recency means a long time has passed since their last purchase. They are the perfect target for retention or win-back campaigns.
</details>

**11.** Are the concepts of "Acquisition" identical in B2B and B2C settings?
<details>
<summary>👉 Show answer</summary>
<b>No.</b> There are substantial differences. In B2B, the importance of <b>risk</b>, <b>turnover</b>, and the <b>relationship</b> is completely different compared to B2C.
</details>
