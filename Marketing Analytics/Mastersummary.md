# Marketing Analytics: Master Exam Study Guide & Self-Assessment Handbook

Welcome to the **Master Exam Study Guide for Marketing Analytics**. This handbook synthesizes all core lecture modules, mathematical frameworks, CRM processes, and analytical metrics from your course materials into a structured, highly actionable study guide.

---

## Table of Contents
1. [Course Foundations & Strategic CRM Framework](#1-course-foundations--strategic-crm-framework)
2. [Customer Lifecycle Processes & Acquisition Strategies](#2-customer-lifecycle-processes--acquisition-strategies)
3. [Value Stimulation, Retention & Win-Back Strategies](#3-value-stimulation-retention--win-back-strategies)
4. [Analytical CRM & Customer Activity Metrics](#4-analytical-crm--customer-activity-metrics)
5. [Perception-Based Metrics & Net Promoter Score (NPS)](#5-perception-based-metrics--net-promoter-score-nps)
6. [Comprehensive Practice Quiz (15 Exam-Style Questions)](#6-comprehensive-practice-quiz)
7. [Revision Flashcards (20 Key Concepts & Formulas)](#7-revision-flashcards)
---

## 1. Course Foundations & Strategic CRM Framework

### 1.1 Academic & Practical Positioning
* **Interdisciplinary Scope**: Marketing Analytics operates at the critical intersection of **Customer Relationship Management (CRM)** and **Digital Marketing**.
* **Objective**: To develop an analytical, data-driven mindset for strategic marketing decisions, combining statistical/quantitative frameworks with practical software tools (e.g., Microsoft Excel, Mailchimp, and Google Analytics 4).

### 1.2 CRM Definition & Core Philosophy
* **Payne & Frow (2005) Definition**: 
  > *"CRM is a strategic marketing approach concerned with creating improved shareholder value through the development of appropriate relationships with key customers and customer segments. CRM unites the potential of relationship marketing strategies and IT to create profitable, long-term relationships with customers and other key stakeholders."*
* **Strategic Reality**: **CRM is not merely software or IT infrastructure; it is a holistic business strategy.**

### 1.3 The Three Forms of CRM (Buttle, 2019)
| CRM Form | Core Definition & Focus | Key Operations / Examples |
| :--- | :--- | :--- |
| **Strategic CRM** | A customer-centric business strategy aimed at winning, developing, and retaining profitable customers over the long term. | Top-level strategic planning, allocation of organizational resources, customer-centric culture. |
| **Operational CRM** | The automation and integration of customer-facing business processes. | Sales Force Automation (SFA), Marketing Automation (DEM/email workflows), Customer Service ticketing. |
| **Analytical CRM** | The systematic process through which organizations transform raw customer data into actionable insights for strategic/operational use. | Customer segmentation, Lifetime Value modeling, Churn risk prediction, Campaign ROI measurement. |

### 1.4 Market & Environmental Contexts
* **B2C vs. B2B Environments**: Differ significantly in terms of risk profile, transaction size, customer turnover rate, decision-making complexity, and relationship length.
* **Contractual vs. Non-Contractual Settings**:
  * **Contractual**: Customer churn is explicitly observed when a contract or subscription is terminated (e.g., Netflix, Mobile Postpaid, Pay-TV).
  * **Non-Contractual**: Customer defection is silent/unobserved (e.g., Grocery retail, E-commerce, Fashion). Marketers must rely on probabilistic models and recency thresholds to infer churn.
---

## 2. Customer Lifecycle Processes & Acquisition Strategies

### 2.1 The Customer Lifecycle Model (Van den Poel, 2013)
The customer relationship follows a dynamic lifecycle trajectory consisting of four main operational stages:
1. **Acquisition**: Identifying, targeting, and converting prospective buyers.
2. **Value Stimulation**: Maximizing spending through Cross-selling and Up-selling.
3. **Retention & Churn Prevention**: Detecting defecting behavior early and implementing targeted incentives to hold active customers.
4. **Reactivation (Win-back)**: Identifying valuable past customers who have lapsed and re-engaging them.

### 2.2 Customer Acquisition Methodologies
* **The Sales Funnel (D’Haen & Van den Poel, 2013)**:
  * **Suspects**: Broad audience with potential interest.
  * **Prospects**: Qualified leads matching ideal target criteria.
  * **Leads**: Prospects showing active interest (10% typical conversion rate from Prospects).
  * **Customers**: Converted leads making a purchase (10% - 50% typical conversion rate from Leads).

* **Lookalike Acquisition Strategy (Blattberg et al., 2004)**:
  1. **Sample**: Extract a representative sample of existing high-value customers.
  2. **Append Data**: Enrich customer records with demographic, behavioral, and transactional data.
  3. **Profile & Cluster**: Cross-tabulate or use clustering algorithms (e.g., k-means) to identify distinguishing traits of high-value segments.
  4. **Target Prospect Databases**: Apply these identified profiles to external prospect databases or ad platforms to find non-customers sharing identical traits.

* **Two-Step Acquisition Strategy**:
  * Utilizes an initial non-purchase interaction (e.g., free webinars, whitepapers, free trials) to allow potential prospects to self-select, followed by a second targeted sales offer.

* **Member-Get-Member (Referral) Programs**:
  * Creates a **win-win-win** structure: existing customers receive a reward (e.g., account credit or commission-free bookings), new prospects receive a discount, and the business acquires qualified leads at low CAC.

### 2.3 Acquisition Metrics & Calculations

#### A. Acquisition Rate
$$\text{Acquisition Rate (\%)} = \left( \frac{\text{Number of Prospects Acquired}}{\text{Total Number of Prospects Targeted}} \right) \times 100$$
* *Example*: If a campaign targets 2,000,000 prospects and successfully converts 60,000, the Acquisition Rate is $\frac{60,000}{2,000,000} \times 100 = 3\%$.

#### B. Customer Acquisition Cost (CAC)
$$\text{CAC} = \frac{\text{Total Acquisition Spending (Marketing + Sales)}}{\text{Number of New Customers Acquired}}$$
* *Cost Elements Included*: Sales & marketing staff salaries, social media ad spend, pay-per-click (PPC) advertising, print/magazine ads, agency fees.
* *Example Calculation*:
  * Sales & Marketing Staff: $150,000
  * Social Media Campaigns: $12,000
  * PPC Advertising: $10,000
  * Magazine Ads: $8,400
  * **Total Expenses**: $180,400 | **New Customers Acquired**: 2,512
  * **CAC** = $\frac{\$180,400}{2,512} = \$71.82$ per customer.
* *Industry Benchmarks (Shopify, 2021)*:
  * Business & Industrial: $533
  * Furniture: $462
  * Electronics: $377
  * Apparel & Shoes: $129
  * Arts & Entertainment: $21
---

## 3. Value Stimulation, Retention & Win-Back Strategies

### 3.1 Value Stimulation: Cross-Selling vs. Up-Selling
* **Cross-Selling (Schmitz et al., 2014)**: Selling **additional, complementary items** that differ from what the customer previously purchased or expressed interest in (e.g., adding shoe polish to a shoe order; bundling internet + TV + mobile services).
  * *Telecom Case Study (Bain & Co.)*: In US telecom where 60% of consumers split services across providers, convincing 10% of users to switch just one service yielded up to $480M in incremental annual revenue.
* **Up-Selling (Salazar et al., 2007)**: Encouraging customers to **upgrade or improve conditions** of their purchase (higher-margin item or higher quantity) to consume more value (e.g., upgrading from standard hotel room to deluxe suite; buying 3 items to get 4th free).

### 3.2 Customer Retention & Churn Management
* **Core Definition**: Ensuring that a customer continues to purchase goods or utilize services over time.
* **Critical Distinction**: **Retaining a customer does NOT necessarily mean making them loyal!** A retained customer may stay out of habit, contractual lock-in, or lack of alternatives.
* **Churn Prevention Strategy (Burez & Van den Poel, 2007)**:
  1. **Develop Predictive Churn Model**: Integrate demographic, financial, transactional, and contact data into a machine learning model to estimate individual churn probabilities.
  2. **Execute Targeted Interventions**: Select the top high-risk decile (e.g., top 30% highest churn probability) and send tailored retention incentives (e.g., free tickets, exclusive discounts, proactive customer service outreach).
* **Paid Subscription Retention Models**: Prime-style paid memberships increase switching costs and dramatically raise purchase frequency.

### 3.3 Win-Back / Reactivation
* **Objective**: Re-engaging past profitable customers who have lapsed or churned.
* **Process**:
  1. Identify historically profitable lapsed customers.
  2. Deploy targeted, personalized incentives (e.g., *"We miss you! Take 30% off your next order"*).
---

## 4. Analytical CRM & Customer Activity Metrics

Customer Activity Metrics form the backbone of behavioral analytics in Analytical CRM.

### 4.1 Purchase Cadence & Regularity

#### A. Inter-Purchase / Inter-Visit Time (IVT)
* **Definition**: The number of elapsed days between two consecutive purchases or visits by a customer.
* **Average IVT**: For $N+1$ transactions, there are $N$ intervals:
  $$\text{Average IVT} = \frac{1}{N} \sum_{i=1}^{N} \text{IVT}_i$$

#### B. Periodicity
* **Definition**: The **standard deviation ($\sigma$)** of a customer's inter-purchase times across all transaction intervals:
  $$\sigma = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2}$$
  *(where $x_i$ is each individual IVT interval, $\mu$ is the mean IVT, and $N$ is the number of intervals)*.
* **Strategic Interpretation**:
  * **Low Periodicity ($\text{Low } \sigma$)**: Represents highly **regular, predictable** shopping behavior (e.g., customer buys every 20 days with minimal variance). Ideal for automated subscription reminders.
  * **High Periodicity ($\text{High } \sigma$)**: Represents **erratic, opportunistic, or seasonal** buying patterns. Requires promotional triggers.

### 4.2 Temporal Relationship Metrics

#### A. Length of Relationship (LoR / Ageing)
* **Definition**: Total number of days elapsed between a customer's **first purchase date** and the benchmark analysis date.
* **Calculation**: $\text{LoR} = \text{Analysis Date} - \text{First Purchase Date}$.
* **Usage**: Differentiates newly acquired patrons from veteran, long-standing clients.

#### B. Recency
* **Definition**: Total number of days elapsed between a customer's **most recent (last) purchase date** and the benchmark analysis date.
* **Calculation**: $\text{Recency} = \text{Analysis Date} - \text{Last Purchase Date}$.
* **Usage**: Key warning metric for dormancy and defection risk. If Recency significantly exceeds the customer's historical Average IVT, retention campaigns should trigger immediately.

---

### 4.3 Cohort Analysis: Retention, Defection, and Survival Rates

When analyzing customer longevity, tracking metrics by **historical customer cohorts** (groups acquired in period $t=0$) prevents aggregation distortions.

#### Formulas Summary
$$\text{Retention Rate } (R_t) = \left( \frac{\text{Active Customers}_t}{\text{Active Customers}_{t-1}} \right) \times 100$$

$$\text{Defection / Churn Rate } (D_t) = \left( \frac{\text{Lapsed Customers}_t}{\text{Active Customers}_{t-1}} \right) \times 100 = 100\% - R_t$$

$$\text{Survival Rate } (S_t) = \left( \frac{\text{Active Customers}_t}{\text{Initial Cohort Base}_0} \right) \times 100$$

#### Comprehensive Step-by-Step Cohort Example
Starting Cohort at Period $t=0$ (2017): **1,000 customers**.

| Period ($t$) | Year | Retained / Active Customers | Defectors (Lost in Period) | Retention Rate ($R_t$) | Defection Rate ($D_t$) | Survival Rate ($S_t$) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **0** | 2017 | **1,000** | 0 | $100\%$ | $0\%$ | $100\%$ |
| **1** | 2018 | **550** | 450 | $\frac{550}{1000} = \mathbf{55.0\%}$ | $\frac{450}{1000} = \mathbf{45.0\%}$ | $\frac{550}{1000} = \mathbf{55.0\%}$ |
| **2** | 2019 | **341** | 209 | $\frac{341}{550} = \mathbf{62.0\%}$ | $\frac{209}{550} = \mathbf{38.0\%}$ | $\frac{341}{1000} = \mathbf{34.1\%}$ |
| **3** | 2020 | **231** | 110 | $\frac{231}{341} = \mathbf{67.7\% \approx 68\%}$ | $\frac{110}{341} = \mathbf{32.3\% \approx 32\%}$ | $\frac{231}{1000} = \mathbf{23.1\%}$ |
| **4** | 2021 | **169** | 62 | $\frac{169}{231} = \mathbf{73.2\% \approx 73\%}$ | $\frac{62}{231} = \mathbf{26.8\% \approx 27\%}$ | $\frac{169}{1000} = \mathbf{16.9\%}$ |

*Key Takeaway*: Notice that while Period 2 Retention Rate is 62% and Defection Rate is 38%, the **Survival Rate in Period 2 is 34.1%** because Survival is referenced against the initial 1,000 base, whereas Retention/Defection are referenced against the prior period's 550 base.

*Commercial Warning*: Industry reports sometimes calculate aggregate annual retention across all active database members without separating by cohort. This mixes newly acquired customers with older cohorts, masking underlying churn trends.

---

### 4.4 Redemption Metrics & Industry Benchmarks

#### A. Coupon & Deal Redemption
* **Coupon-Level Redemption Rate**: $\frac{\text{Number of Coupons Redeemed}}{\text{Total Number of Coupons Issued}} \times 100$
* **Customer-Level Redemption Rate**: $\frac{\text{Number of Unique Redeemers}}{\text{Total Number of Targeted Customers Receiving Coupon}} \times 100$

#### B. Loyalty Program Redemption
* **Points-Level Redemption Rate**: $\frac{\text{Number of Points Redeemed for Rewards}}{\text{Total Number of Points Issued}} \times 100$
* **Member Redemption Rate**: $\frac{\text{Number of Active Redeemers}}{\text{Total Number of Loyalty Program Members}} \times 100$

#### C. Industry Benchmarks
* **Standard Couponing Campaigns**: $3\% - 25\%$
* **Instant Win Campaigns**: $3\% - 10\%$
* **Short-Term Collection / Loyalty Programs**: $10\% - 40\%$
---

## 5. Perception-Based Metrics & Net Promoter Score (NPS)

### 5.1 Customer Satisfaction (CSAT)
* Measured via survey Likert scales ($1\text{--}5$ or $1\text{--}7$).
* Assesses emotional delight, agreement with service quality, and overall fit.

### 5.2 Net Promoter Score (NPS) Methodology (Reichheld, 2003)
Introduced in Harvard Business Review (*"The One Number You Need to Grow"*), NPS measures customer advocacy and loyalty using a single question:
> *"How likely is it that you would recommend [Company X] to a friend or colleague?"* (Scale $0$ to $10$).

#### Customer Categorization
* **Promoters (Score 9–10)**: Extremely loyal advocates whose lives have been enriched by the company. They demonstrate high repeat purchase rates, allocate a high share of wallet, and generate positive word-of-mouth.
* **Passives / Passively Satisfied (Score 7–8)**: Satisfied but not emotionally loyal. They make few referrals and are highly susceptible to switching if competitors offer discounts.
* **Detractors (Score 0–6)**: Dissatisfied customers who feel aggrieved. They generate negative word-of-mouth, file frequent complaints (raising cost-to-serve), degrade team morale, and churn quickly.

#### NPS Formula
$$\text{NPS} = \% \text{Promoters} - \% \text{Detractors}$$
*(Passives are included in the total survey sample denominator, effectively lowering the percentage weight of Promoters and Detractors).*
* *Range*: $-100$ (all Detractors) to $+100$ (all Promoters).

---

### 5.3 Pitfalls, Manipulation & Best Practices in NPS

#### Common Misuses & Distortions
* **Incentive Alignment Flaws**: Linking frontline employee compensation directly to NPS scores causes employees to focus on rating manipulation rather than genuine service quality.
* **Pleading & Informal Deals**: Staff begging customers for top ratings (*"I will lose my job if you don't give me a 10"*) or offering perks (*"Free service for a 10 rating"*).
* **Sampling Bias & Selective Filtering**: Omitting dissatisfied clients (e.g., suppressing surveys for customers whose insurance claims were denied).
* **Vanity Statistics**: Reporting public NPS scores without response rate context, transaction triggers, or third-party double-blind validation.

#### Recommended NPS Best Practices
1. Maintain high response rates across representative customer bases.
2. Separate **Transactional NPS** (tied to specific touchpoints) from **Relational NPS** (overall brand perception).
3. Ensure survey anonymity to eliminate pleading or rating distortion.
4. **Link NPS metrics to actual behavioral transaction data** (e.g., verifying if Promoters actually purchase more over time).
5. Leverage standardized competitive benchmark services such as **NPS Prism (Bain & Co.)**.
---

## 6. Comprehensive Practice Quiz

Test your mastery with these 15 exam-style practice questions. Detailed explanations are provided at the end of the section.

### Question 1
A customer cohort begins with 1,000 active customers in Period 0. In Period 1, 550 customers are retained. In Period 2, 341 customers remain active. What is the **Defection (Churn) Rate in Period 2**?
* A) 34.1%
* B) 38.0%
* C) 62.0%
* D) 20.9%

### Question 2
In the standard Lookalike Acquisition Strategy framework outlined by Blattberg et al. (2004), what step immediately follows sampling current customers and appending demographic/characteristic data?
* A) Calculating Customer Acquisition Cost (CAC) for each segment.
* B) Cross-tabulating or using clustering techniques to profile current customers based on those traits.
* C) Executing an automated DEM email campaign.
* D) Purchasing non-customer contact lists from external brokers.

### Question 3
According to Van den Poel (2013) and Buttle (2019), which of the following statements regarding Customer Retention is CORRECT?
* A) Retaining a customer is mathematically identical to making them loyal.
* B) Retaining customers eliminates the need for customer acquisition investments.
* C) Customer retention can apply to service usage even in unpaid settings.
* D) Retention rates should only be measured in contractual B2B settings.

### Question 4
A retail bank spends $150,000 on sales staff, $12,000 on social ads, $10,000 on PPC, and $8,400 on magazine ads. If they acquire 2,512 new accounts, what is their Customer Acquisition Cost (CAC)?
* A) $59.71
* B) $71.82
* C) $129.00
* D) $462.00

### Question 5
What is the primary difference between **Recency** and **Periodicity** in Analytical CRM?
* A) Recency measures the standard deviation of visits, whereas Periodicity measures days since first purchase.
* B) Recency evaluates timeliness (days since last purchase), whereas Periodicity measures the variance/regularity of inter-visit times.
* C) Recency is used for B2B markets, while Periodicity is strictly B2C.
* D) Recency measures survival rate, while Periodicity calculates CAC.

### Question 6
If a customer makes purchases on Day 1, Day 20, Day 39, and Day 59, what is their **Average Inter-Purchase Time (IVT)**?
* A) 19.33 days
* B) 14.75 days
* C) 20.00 days
* D) 29.50 days

### Question 7
In an NPS survey of 500 customers, 250 rate the firm a 9 or 10, 150 rate the firm a 7 or 8, and 100 rate the firm between 0 and 6. What is the **Net Promoter Score**?
* A) +50
* B) +30
* C) +20
* D) +150

### Question 8
Which customer group in the NPS methodology is described as having their lives "diminished" by dealings with the firm, driving up service costs and generating negative word-of-mouth?
* A) Passives
* B) Lapsed Prospects
* C) Detractors
* D) Suspects

### Question 9
Why is linking frontline employee compensation directly to Net Promoter Scores considered a major pitfall?
* A) It lowers the overall acquisition rate.
* B) It incentivizes manipulation, pleading, perks, and survey cherry-picking.
* C) It increases the standard deviation of inter-visit times.
* D) It turns contractual settings into non-contractual settings.

### Question 10
What is the **Survival Rate** in Period 3 for a cohort that starts with 1,000 customers at Period 0 and has 231 active customers remaining in Period 3?
* A) 68.0%
* B) 32.0%
* C) 23.1%
* D) 67.7%

### Question 11
Which of the following is an example of **Up-Selling**?
* A) Recommending a camera bag when a customer buys a camera.
* B) Encouraging a hotel guest to upgrade from a standard room to a luxury suite.
* C) Sending a "We Miss You" 30% discount to a churned customer.
* D) Partnering with a bank to offer credit card cash-back rewards.

### Question 12
According to Payne and Frow (2005), what is the primary overarching goal of CRM?
* A) Automating 100% of customer service calls via AI.
* B) Creating improved shareholder value through appropriate customer relationships and IT integration.
* C) Maximizing coupon redemption rates across all demographics.
* D) Eliminating natural customer turnover completely.

### Question 13
What characterizes a customer with **Low Periodicity**?
* A) They buy erratically with long, unpredictable gaps.
* B) They purchase at fixed, highly predictable intervals with minimal variance.
* C) They have high recency and high defection rates.
* D) They respond exclusively to win-back campaigns.

### Question 14
Which redemption benchmark range is typical for **Short-Term Loyalty Collection Campaigns**?
* A) 3% - 10%
* B) 3% - 25%
* C) 10% - 40%
* D) 50% - 80%

### Question 15
In the Burez & Van den Poel (2007) Pay-TV study, how was the churn prevention strategy structured?
* A) Sending retention offers to all customers indiscriminately.
* B) Using predictive churn models to identify the top 30% highest-risk customers and executing targeted field interventions.
* C) Raising subscription fees to force uncommitted users to defect.
* D) Replacing operational CRM with strategic CRM.

---

### Answer Key & Explanations

1. **Correct Answer: B (38.0%)**
   * *Explanation*: In Period 1, there were 550 active customers. In Period 2, 341 remained active, meaning $550 - 341 = 209$ defected. The Period 2 Defection Rate is referenced against Period 1 active customers: $\frac{209}{550} \times 100 = 38.0\%$. (Note: 34.1% is the *Survival Rate*, not the Period 2 Defection Rate!).

2. **Correct Answer: B**
   * *Explanation*: The Blattberg et al. (2004) process consists of: (1) Sample current customers, (2) Append demographic/characteristic data, (3) Cross-tabulate/cluster to profile traits, and (4) Apply profiles to prospect databases.

3. **Correct Answer: C**
   * *Explanation*: Retention measures continued product or service usage over time, which applies even to unpaid digital services (e.g., email or free app usage). Retaining does not equal loyalty, nor does it remove the need for acquisition.

4. **Correct Answer: B ($71.82)**
   * *Explanation*: Total expenses = $\$150,000 + \$12,000 + \$10,000 + \$8,400 = \$180,400$. CAC = $\frac{\$180,400}{2,512} = \$71.82$.

5. **Correct Answer: B**
   * *Explanation*: Recency measures the elapsed days since the last purchase (timeliness/dormancy), whereas Periodicity is the standard deviation ($\sigma$) of inter-visit times (regularity/predictability).

6. **Correct Answer: A (19.33 days)**
   * *Explanation*: The intervals between purchases are: Interval 1 = $20-1 = 19$ days; Interval 2 = $39-20 = 19$ days; Interval 3 = $59-39 = 20$ days. Average IVT = $\frac{19 + 19 + 20}{3} = \frac{58}{3} = 19.33$ days.

7. **Correct Answer: B (+30)**
   * *Explanation*: $\% \text{Promoters} = \frac{250}{500} = 50\%$. $\% \text{Passives} = \frac{150}{500} = 30\%$. $\% \text{Detractors} = \frac{100}{500} = 20\%$. $\text{NPS} = 50\% - 20\% = +30$.

8. **Correct Answer: C (Detractors)**
   * *Explanation*: Detractors (scores 0–6) represent disaffected customers who make complaints, degrade morale, and drive up cost-to-serve.

9. **Correct Answer: B**
   * *Explanation*: High-stakes employee bonuses linked directly to NPS lead to pleading (*"give me a 10"*), perks, and selective survey distribution, destroying data integrity.

10. **Correct Answer: C (23.1%)**
    * *Explanation*: Survival Rate always references the starting Period 0 base (1,000). Survival Rate in Period 3 = $\frac{231}{1000} \times 100 = 23.1\%$.

11. **Correct Answer: B**
    * *Explanation*: Up-selling involves upgrading the condition or margin of an existing product category (e.g., standard room to deluxe suite). Recommending a camera bag is cross-selling.

12. **Correct Answer: B**
    * *Explanation*: Payne & Frow (2005) explicitly state that CRM's goal is creating improved shareholder value through appropriate customer relationships and IT integration.

13. **Correct Answer: B**
    * *Explanation*: Periodicity is standard deviation ($\sigma$). A low standard deviation means purchase intervals vary very little from the mean, indicating highly regular shopping.

14. **Correct Answer: C (10% - 40%)**
    * *Explanation*: Course material specifies benchmarks: Couponing (3-25%), Instant Win (3-10%), Short Loyalty Collections (10-40%).

15. **Correct Answer: B**
    * *Explanation*: Burez & Van den Poel (2007) built a predictive churn model, identified the top 30% highest-risk customers, and executed targeted retention offers in a field experiment.
---

## 7. Revision Flashcards

Use these 20 flashcards for rapid key-term revision before your exam.

### Card 1
* **FRONT**: What is Strategic CRM?
* **BACK**: A customer-centric business strategy aimed at winning, developing, and retaining profitable customers (Buttle, 2019).

### Card 2
* **FRONT**: What is Operational CRM?
* **BACK**: The automation and integration of customer-facing processes such as sales, marketing automation, and customer service.

### Card 3
* **FRONT**: What is Analytical CRM?
* **BACK**: The process of transforming customer data into actionable insights for strategic and operational decision-making.

### Card 4
* **FRONT**: Formula for Customer Acquisition Cost (CAC)
* **BACK**: $\text{CAC} = \frac{\text{Total Acquisition Spending (Marketing + Sales)}}{\text{Number of New Customers Acquired}}$

### Card 5
* **FRONT**: What are the 4 steps of Lookalike Targeting (Blattberg et al., 2004)?
* **BACK**: (1) Sample current customers -> (2) Append demographic/behavioral data -> (3) Cluster/profile traits -> (4) Apply profile to prospect databases/ad platforms.

### Card 6
* **FRONT**: Define Cross-Selling vs. Up-Selling
* **BACK**: **Cross-selling**: Selling additional complementary items from different categories. **Up-selling**: Upgrading an existing product to a higher-margin or higher-spec version.

### Card 7
* **FRONT**: What is Inter-Purchase / Inter-Visit Time (IVT)?
* **BACK**: The number of elapsed days between two consecutive purchases or visits by a single customer.

### Card 8
* **FRONT**: What is Periodicity in Customer Analytics?
* **BACK**: The standard deviation ($\sigma$) of a customer's inter-purchase times. Low $\sigma$ = regular buyer; High $\sigma$ = erratic buyer.

### Card 9
* **FRONT**: Define Recency
* **BACK**: The number of days elapsed between a customer's **most recent (last) purchase date** and the analysis benchmark date. Used to signal churn risk.

### Card 10
* **FRONT**: Define Length of Relationship (LoR / Ageing)
* **BACK**: The total number of days elapsed between a customer's **first purchase date** and the analysis benchmark date.

### Card 11
* **FRONT**: Formula for Cohort Retention Rate ($R_t$)
* **BACK**: $R_t = \left( \frac{\text{Active Customers}_t}{\text{Active Customers}_{t-1}} \right) \times 100$

### Card 12
* **FRONT**: Formula for Cohort Defection / Churn Rate ($D_t$)
* **BACK**: $D_t = \left( \frac{\text{Lapsed Customers}_t}{\text{Active Customers}_{t-1}} \right) \times 100 = 100\% - R_t$

### Card 13
* **FRONT**: Formula for Cohort Survival Rate ($S_t$)
* **BACK**: $S_t = \left( \frac{\text{Active Customers}_t}{\text{Initial Cohort Base}_0} \right) \times 100$ (Always references Period 0!).

### Card 14
* **FRONT**: How is Net Promoter Score (NPS) calculated?
* **BACK**: $\text{NPS} = \% \text{Promoters (9-10)} - \% \text{Detractors (0-6)}$. Passives (7-8) are included in the total sample denominator.

### Card 15
* **FRONT**: What characterizes "Promoters" in NPS?
* **BACK**: Customers scoring 9–10 who have enriched relationships, high repeat purchases, high share of wallet, and strong word-of-mouth advocacy.

### Card 16
* **FRONT**: What characterizes "Passives" in NPS?
* **BACK**: Customers scoring 7–8 who are passively satisfied but not loyal. They make few referrals and easily switch if competitors offer discounts.

### Card 17
* **FRONT**: What characterizes "Detractors" in NPS?
* **BACK**: Customers scoring 0–6 who feel aggrieved, generate negative word-of-mouth, degrade team morale, and drive up service costs through complaints.

### Card 18
* **FRONT**: Name three major pitfalls in corporate NPS execution
* **BACK**: (1) Linking frontline bonuses to NPS (incentivizes gaming), (2) Pleading/perks for 10s, (3) Cherry-picking/suppressing unhappy customers from surveys.

### Card 19
* **FRONT**: Benchmark redemption ranges for Couponing vs. Loyalty Programs
* **BACK**: Couponing: 3% - 25%; Instant Win: 3% - 10%; Short Loyalty Collections: 10% - 40%.

### Card 20
* **FRONT**: Contractual vs. Non-Contractual Churn Settings
* **BACK**: **Contractual**: Churn is explicitly observed upon cancellation. **Non-contractual**: Churn is unobserved/silent and must be statistically inferred from Recency and IVT.
