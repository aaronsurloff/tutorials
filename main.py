import streamlit as st
import pandas as pd

# --- Main Navigation ---
def main():
    st.set_page_config(page_title="Comprehensive Accounting Course", layout="wide")
    st.sidebar.title("Course Navigation")
    pages = [
        "Introduction",
        "Module 1: Accounting Fundamentals & the 5 Categories",
        "Module 2: Journal Entries, Accruals & Balancing",
        "Module 3: Managing the Chart of Accounts",
        "Module 4: Budgeting, Forecasting & Consolidation",
        "Module 5: Real Estate Practices & Product Integration",
        "Module 6: Review & Assessment",
    ]
    choice = st.sidebar.radio("Go to", pages)
    
    if choice == pages[0]:
        show_introduction()
    elif choice == pages[1]:
        show_module1()
    elif choice == pages[2]:
        show_module2()
    elif choice == pages[3]:
        show_module3()
    elif choice == pages[4]:
        show_module4()
    elif choice == pages[5]:
        show_module5()
    elif choice == pages[6]:
        show_module6()

# --- Module Functions ---

def show_introduction():
    st.title("Comprehensive Accounting for Real Estate & Leasing")
    st.markdown("""
    **Objective:**  
    This course is designed to give product managers and engineers a thorough, hands-on understanding of accounting concepts in the real estate and leasing context. You will:
    - Learn the five fundamental categories: **Assets, Liabilities, Equity, Revenue, and Expenses**.
    - Understand how every transaction is recorded as balanced debits and credits.
    - Simulate the creation of accruals and their reversing entries.
    - Build and manage your own Chart of Accounts.
    - Explore budgeting, forecasting, consolidation, and real‑world lease accounting.
    
    Use the sidebar to navigate through the modules. Each module combines teaching with interactive examples and quizzes.
    """)

def show_module1():
    st.header("Module 1: Accounting Fundamentals & the 5 Categories")
    st.markdown("### Teaching Section")
    with st.expander("Learn the Basics", expanded=True):
        st.markdown("""
        In accounting, every transaction falls into one of five key categories:
        
        **Assets:**  
        - Resources owned by a business (e.g., Cash, Property, Equipment).
        
        **Liabilities:**  
        - Debts or obligations (e.g., Loans, Accounts Payable, Accrued Expenses).
        
        **Equity:**  
        - The residual interest after liabilities are deducted from assets (e.g., Owner’s Equity, Retained Earnings).
        
        **Revenue:**  
        - Income earned from business operations (e.g., Rental Income, Sales Revenue).
        
        **Expenses:**  
        - Costs incurred in generating revenue (e.g., Maintenance, Utilities, Marketing).
        
        **Double-Entry Principle:**  
        Every transaction is recorded with at least one debit and one credit. For a balanced entry, total debits must equal total credits.
        """)
        st.markdown("**Example Transaction: A company receives $2,000 in rental income.**")
        rental_data = {
            "Category": ["Asset", "Revenue", "Asset", "Asset"],
            "Account": ["Accounts Receivable", "Rental Income", "Cash", "Accounts Receivable"],
            "Date": ["10/1", "10/1", "10/3", "10/3"],
            "Debit": [2000, 0, 2000, 0],
            "Credit": [0, 2000, 0, 2000]
            
        }
        rental_df = pd.DataFrame(rental_data)
        st.table(rental_df)
    
    st.markdown("### Quiz: Transaction Recording for a Pipe Replacement")
    st.markdown("""
    **Scenario:**  
    A $500 pipe replacement is performed on March 18th, and you receive an invoice. The invoice is due on April 1st, and payment is made on April 1st.
    
    **Instructions:**  
    Fill in the tables below:
    - **Invoice Receipt (March 18th):** Record the accrual transaction when you receive the invoice.  
      *Hint: Debit the appropriate Expense account and Credit a Liability account (e.g., Accrued Expenses or Accounts Payable).*
    - **Payment (April 1st):** Record the payment transaction when you pay the invoice.  
      *Hint: Debit the Liability account and Credit Cash.*
    """)
    
    invoice_account_options = ["Pipe Replacement Expense", "Maintenance Expense", "Accounts Payable", "Accrued Expenses"]
    payment_account_options = ["Accounts Payable", "Accrued Expenses", "Cash"]
    entry_type_options = ["Debit", "Credit"]
    
    st.markdown("#### Invoice Receipt (March 18th)")
    invoice_df = pd.DataFrame({
        "Account": ["", ""],
        "Entry Type": ["", ""],
        "Amount ($)": [0, 0]
    }, index=["Line 1", "Line 2"])
    edited_invoice_df = st.data_editor(
        invoice_df,
        num_rows="fixed",
        key="invoice_editor",
        column_config={
            "Account": st.column_config.SelectboxColumn("Account", options=invoice_account_options),
            "Entry Type": st.column_config.SelectboxColumn("Entry Type", options=entry_type_options),
        }
    )
    
    st.markdown("#### Payment (April 1st)")
    payment_df = pd.DataFrame({
        "Account": ["", ""],
        "Entry Type": ["", ""],
        "Amount ($)": [0, 0]
    }, index=["Line 1", "Line 2"])
    edited_payment_df = st.data_editor(
        payment_df,
        num_rows="fixed",
        key="payment_editor",
        column_config={
            "Account": st.column_config.SelectboxColumn("Account", options=payment_account_options),
            "Entry Type": st.column_config.SelectboxColumn("Entry Type", options=entry_type_options),
        }
    )
    
    if st.button("Submit Answers for Quiz", key="submit_quiz_mod1_table"):
        st.markdown("### Your Submitted Answers")
        st.write("#### Invoice Receipt (March 18th)")
        st.table(edited_invoice_df)
        st.write("#### Payment (April 1st)")
        st.table(edited_payment_df)
        st.markdown("**Expected Answer:**")
        st.markdown("""
        **Invoice Receipt (March 18th):**  
        - **Line 1:** Debit: Pipe Replacement Expense (or Maintenance Expense) $500  
        - **Line 2:** Credit: Accounts Payable (or Accrued Expenses) $500  
        
        **Payment (April 1st):**  
        - **Line 1:** Debit: Accounts Payable (or Accrued Expenses) $500  
        - **Line 2:** Credit: Cash $500  
        """)
        st.success("Review your submitted answers against the expected answers above.")

def show_module2():
    st.header("Module 2: Journal Entries, Accruals & Balancing")
    st.markdown("### Teaching Section")
    with st.expander("Recording Transactions & Accruals", expanded=True):
        st.markdown("""
        **Journal Entries:**  
        Every transaction is recorded with debits and credits that must balance.
        
        **Accruals:**  
        Record revenues or expenses when they occur—even if cash hasn’t changed hands.
        - *Example:* If a $500 repair expense is incurred in December but paid in January, record an accrual in December.
        
        **Reversing Entries:**  
        In the following period, a reversing entry cancels out the accrual.
        
        **Example of an Accrual Entry:**  
        - **Debit:** Repair Expense $500  
        - **Credit:** Accrued Expenses $500
        
        **Reversing Entry:**  
        - **Debit:** Accrued Expenses $500  
        - **Credit:** Repair Expense $500
        """)
    
    st.markdown("### Interactive Exercise: Record a Repair Expense Accrual")
    accrual_df = pd.DataFrame({
        "Account": ["", ""],
        "Entry Type": ["", ""],
        "Amount ($)": [0, 0]
    }, index=["Line 1", "Line 2"])
    edited_accrual_df = st.data_editor(
        accrual_df,
        num_rows="fixed",
        key="accrual_editor",
        column_config={
            "Account": st.column_config.SelectboxColumn("Account", options=["Repair Expense", "Accrued Expenses"]),
            "Entry Type": st.column_config.SelectboxColumn("Entry Type", options=["Debit", "Credit"]),
        }
    )
    if st.button("Submit Accrual Entry", key="submit_accrual_entry"):
        try:
            df = edited_accrual_df
            total_debits = df[df["Entry Type"] == "Debit"]["Amount ($)"].sum()
            total_credits = df[df["Entry Type"] == "Credit"]["Amount ($)"].sum()
        except Exception as e:
            st.error("Error calculating totals. Ensure all amounts are numeric.")
            total_debits = total_credits = 0
        
        st.markdown("**Your Accrual Journal Entry:**")
        st.table(edited_accrual_df)
        st.write("Total Debits: $", total_debits)
        st.write("Total Credits: $", total_credits)
        if total_debits == total_credits and total_debits > 0:
            st.success("Balanced Entry: Debits equal Credits!")
        else:
            st.error("Unbalanced Entry: Please ensure total debits equal total credits.")
    
    st.markdown("### Interactive Exercise: Record a Reversing Entry")
    reversing_df = pd.DataFrame({
        "Account": ["", ""],
        "Entry Type": ["", ""],
        "Amount ($)": [0, 0]
    }, index=["Line 1", "Line 2"])
    edited_reversing_df = st.data_editor(
        reversing_df,
        num_rows="fixed",
        key="reversing_editor",
        column_config={
            "Account": st.column_config.SelectboxColumn("Account", options=["Accrued Expenses", "Repair Expense"]),
            "Entry Type": st.column_config.SelectboxColumn("Entry Type", options=["Debit", "Credit"]),
        }
    )
    if st.button("Submit Reversing Entry", key="submit_reversing_entry"):
        try:
            rev_df = edited_reversing_df
            total_debits_rev = rev_df[rev_df["Entry Type"] == "Debit"]["Amount ($)"].sum()
            total_credits_rev = rev_df[rev_df["Entry Type"] == "Credit"]["Amount ($)"].sum()
        except Exception as e:
            st.error("Error calculating totals for reversing entry.")
            total_debits_rev = total_credits_rev = 0
        
        st.markdown("**Your Reversing Journal Entry:**")
        st.table(edited_reversing_df)
        st.write("Total Debits: $", total_debits_rev)
        st.write("Total Credits: $", total_credits_rev)
        if total_debits_rev == total_credits_rev and total_debits_rev > 0:
            st.success("Balanced Entry: Debits equal Credits!")
        else:
            st.error("Unbalanced Entry: Please ensure total debits equal total credits.")
    
    st.markdown("### Hands-On: Simulate Your Own Journal Entry")
    with st.expander("Enter details for a new transaction", expanded=True):
        debit_account = st.text_input("Debit Account", "Cash", key="debit_account_own")
        debit_amt = st.number_input("Debit Amount ($)", min_value=0.0, value=1000.0, step=50.0, key="debit_amt_own")
        credit_account = st.text_input("Credit Account", "Rental Income", key="credit_account_own")
        credit_amt = st.number_input("Credit Amount ($)", min_value=0.0, value=1000.0, step=50.0, key="credit_amt_own")
        if st.button("Submit Journal Entry", key="submit_journal_own"):
            st.markdown("**Your Journal Entry:**")
            st.markdown(f"- **Debit:** {debit_account} ${debit_amt}")
            st.markdown(f"- **Credit:** {credit_account} ${credit_amt}")
            if debit_amt == credit_amt:
                st.success("Balanced Entry: Debits equal Credits!")
            else:
                st.error("Unbalanced Entry: Please ensure total debits equal total credits.")

def show_module3():
    st.header("Module 3: Managing the Chart of Accounts")
    st.markdown("### Teaching Section: Chart of Accounts Overview")
    with st.expander("What is a Chart of Accounts?", expanded=True):
        st.markdown("""
        A Chart of Accounts (COA) is an organized listing of all accounts in your accounting system, grouped into the five fundamental categories:
        
        1. **Assets:** e.g., Cash, Accounts Receivable, Property Assets.
        2. **Liabilities:** e.g., Loans, Accrued Expenses.
        3. **Equity:** e.g., Owner’s Equity, Retained Earnings.
        4. **Revenue:** e.g., Rental Income, Service Revenue.
        5. **Expenses:** e.g., Maintenance, Utilities, Marketing.
        
        A well-structured COA allows you to record transactions accurately and generate financial statements that inform decision-making.
        """)

    st.markdown("### Interactive Exercise: Build Your Chart of Accounts")
    st.markdown("For each fundamental category, select the appropriate account from the dropdown below. Your answer will be compared to the correct account.")

    # Define the five categories.
    categories = ["Assets", "Liabilities", "Equity", "Revenue", "Expenses"]

    # Remove any default by prepending an empty string.
    account_options = {
        "Assets": ["", "Accrued Expenses", "Unpaid Vendor Invoice", "Cash", "Retained Earnings", "Maintenance", "Rental Income"],
        "Liabilities": ["", "Accrued Expenses", "Unpaid Vendor Invoice", "Cash", "Retained Earnings", "Maintenance", "Rental Income"],
        "Equity": ["", "Accrued Expenses", "Unpaid Vendor Invoice", "Cash", "Retained Earnings", "Maintenance", "Rental Income"],
        "Revenue": ["", "Accrued Expenses", "Unpaid Vendor Invoice", "Cash", "Retained Earnings", "Maintenance", "Rental Income"],
        "Expenses": ["", "Accrued Expenses", "Unpaid Vendor Invoice", "Cash", "Retained Earnings", "Maintenance", "Rental Income"]
    }

    # Define the correct mapping.
    correct_mapping = {
        "Assets": "Cash",
        "Liabilities": "Unpaid Vendor Invoice",
        "Equity": "Retained Earnings",
        "Revenue": "Rental Income",
        "Expenses": "Maintenance"
    }

    # Create a list to store the user selections.
    coa_entries = []
    for category in categories:
        selected_account = st.selectbox(f"Select the correct {category} Account", 
                                        options=account_options[category], 
                                        key=f"{category}_account")
        coa_entries.append({
            "Category": category, 
            "Your Answer": selected_account, 
            "Correct Answer": correct_mapping[category]
        })

    if st.button("Submit Chart of Accounts", key="submit_coa_custom"):
        coa_df = pd.DataFrame(coa_entries)
        st.markdown("### Your Chart of Accounts")
        st.table(coa_df)
        # Display correctness feedback for each category.
        for idx, row in coa_df.iterrows():
            if row["Your Answer"] == row["Correct Answer"]:
                st.write(f"**{row['Category']}**: Correct!")
            else:
                st.write(f"**{row['Category']}**: Incorrect. The correct account is **{row['Correct Answer']}**.")

def show_module4():
    st.header("Module 4: Budgeting, Forecasting & Consolidation")
    st.markdown("### Teaching Section: Financial Planning")
    with st.expander("Budgeting & Forecasting Basics", expanded=True):
        st.markdown("""
        **Budgeting:**  
        - Create financial plans for property operations.
        - Include projected revenues and anticipated expenses.
        
        **Forecasting:**  
        - Use historical data and trends to predict future performance.
        - Consider various scenarios to plan for potential changes.
        
        **Consolidation:**  
        - Combine financial data from multiple properties.
        - Adjust for intercompany transactions to produce a single, coherent financial statement.
        """)
    
    st.markdown("### Interactive Exercise: Budget Builder")
    st.markdown("Imagine a property with the following monthly details:")
    st.write("- **Rental Income:** $5,000")
    st.write("- **Expenses:** Maintenance $800, Utilities $300, Marketing $400")
    rental_income = st.number_input("Monthly Rental Income ($)", value=5000, step=100, key="mod4_rental")
    maintenance = st.number_input("Maintenance Expense ($)", value=800, step=50, key="mod4_maintenance")
    utilities = st.number_input("Utilities Expense ($)", value=300, step=50, key="mod4_utilities")
    marketing = st.number_input("Marketing Expense ($)", value=400, step=50, key="mod4_marketing")
    total_expenses = maintenance + utilities + marketing
    net_income = rental_income - total_expenses
    st.write("**Calculated Monthly Net Income:** $", net_income)
    
    months = [f"Month {i}" for i in range(1, 7)]
    forecast_df = pd.DataFrame({
        "Rental Income": [rental_income]*6,
        "Total Expenses": [total_expenses]*6,
        "Net Income": [net_income]*6
    }, index=months)
    st.dataframe(forecast_df)
    st.line_chart(forecast_df[["Rental Income", "Total Expenses", "Net Income"]])
    
    st.markdown("### Quiz: Why Reconcile Budgets?")
    recon_answer = st.text_area("Explain why it’s important to reconcile budgets with actuals:", key="mod4_quiz_answer")
    if st.button("Submit Answer - Module 4", key="submit_mod4_answer"):
        st.write("Your response:")
        st.write(recon_answer)
        st.info("Reconciliation helps identify variances, improves forecasting, and ensures financial accuracy.")

def show_module5():
    st.header("Module 5: Real Estate Practices & Product Integration")
    st.markdown("### Teaching Section: Real Estate Specifics")
    with st.expander("Lease Accounting & Operational Metrics", expanded=True):
        st.markdown("""
        **Lease Accounting:**  
        - **Revenue Recognition:** How and when rental income is recorded.
        - **Depreciation:** Spreading the cost of property assets over their useful lives.
        - **Lease Incentives:** Concessions (discounts) that are spread evenly over the lease term.
        
        **Operational Metrics:**  
        - Track key performance indicators (KPIs) such as occupancy rate and net operating income.
        - Integrate real-time financial data into property management dashboards.
        """)
    
    st.markdown("### Interactive Exercise: Lease Incentive Simulator")
    # Force selection with a "Please select" option.
    lease_term_options = ["Please select", 12, 24, 36]
    lease_term = st.selectbox("Lease Term (months)", options=lease_term_options, key="lease_term")
    
    total_incentive = st.number_input("Total Incentive Discount ($)", value=0, step=100, key="lease_incentive")
    
    if lease_term != "Please select" and total_incentive > 0:
        monthly_adjustment = total_incentive / lease_term
        st.write("Monthly incentive adjustment: $", monthly_adjustment)
    else:
        monthly_adjustment = None
        st.write("Please select a lease term and enter a total incentive discount.")
    
    st.markdown("### Challenge: Configure the Recurring Journal Entry for the Lease Incentive")
    st.markdown("""
    To record the lease incentive discount over the life of the lease, a recurring journal entry is established.
    This configuration will apply the monthly entry repeatedly so that the total over the lease term equals the total incentive discount.
    
    For each recurring entry, your configuration should include a Debit and Credit line!
    """)
    
    if monthly_adjustment is not None:
        # Prepare a table for user configuration (for input only, not used for output).
        lease_entry_df = pd.DataFrame({
            "Category": ["", ""],
            "Account": ["", ""],
            "Entry Type": ["", ""],
            "Amount ($)": [0, 0],
            "Cadence": ["", ""],
            "Duration": [0, 0]
        }, index=["Line 1", "Line 2"])
        # Dropdown options for configuration.
        category_options = ["", "Asset", "Liability", "Equity", "Revenue", "Expense"]
        lease_account_options = ["", "Concessions", "Rental Income"]
        lease_entry_type_options = ["Debit", "Credit"]
        cadence_options = ["", "Monthly", "Weekly", "Annually"]
        
        edited_lease_entry_df = st.data_editor(
            lease_entry_df,
            num_rows="fixed",
            key="lease_entry_editor",
            column_config={
                "Category": st.column_config.SelectboxColumn("Category", options=category_options),
                "Account": st.column_config.SelectboxColumn("Account", options=lease_account_options),
                "Entry Type": st.column_config.SelectboxColumn("Entry Type", options=lease_entry_type_options),
                "Cadence": st.column_config.SelectboxColumn("Cadence", options=cadence_options)
            }
        )
        
        st.markdown("When finished, click the button to submit your recurring journal entry configuration.")
        if st.button("Submit Recurring Journal Entry", key="submit_lease_entry"):
            # Instead of using the user's configuration, output the correct answer.
            expected_config = pd.DataFrame({
                "Category": ["Expense", "Revenue"],
                "Account": ["Concessions", "Rental Income"],
                "Entry Type": ["Debit", "Credit"],
                "Amount ($)": [monthly_adjustment, monthly_adjustment],
                "Cadence": ["Monthly", "Monthly"],
                "Duration": [lease_term, lease_term]
            }, index=["Line 1", "Line 2"])
            st.markdown("### Correct Recurring Journal Entry Configuration")
            st.table(expected_config)
            
            # Generate a schedule for the entire lease term.
            months = list(range(1, int(lease_term) + 1))
            schedule_rows = []
            for m in months:
                schedule_rows.append({
                    "Month": m,
                    "Category": "Expense",
                    "Account": "Concessions",
                    "Entry Type": "Debit",
                    "Amount ($)": monthly_adjustment
                })
                schedule_rows.append({
                    "Month": m,
                    "Category": "Revenue",
                    "Account": "Rental Income",
                    "Entry Type": "Credit",
                    "Amount ($)": monthly_adjustment
                })
            expected_schedule = pd.DataFrame(schedule_rows)
            st.markdown("### Recurring Journal Entry Schedule")
            st.table(expected_schedule)
            st.markdown(f"Over {lease_term} months, the total lease incentive will be ${monthly_adjustment * lease_term:.2f}.")
            st.success("Review the recurring schedule to understand how the entry is applied over the lease term.")

def show_module6():
    st.header("Module 6: Review & Assessment")
    st.markdown("### Final Multiple Choice Quiz")
    
    # Question 1
    q1 = st.radio(
        "1. What are the three primary financial statements?",
        options=[
            "Please select",
            "Balance Sheet, Income Statement, Cash Flow Statement",
            "Balance Sheet, Trial Balance, General Ledger",
            "Income Statement, Statement of Retained Earnings, and Statement of Changes in Equity"
        ],
        key="q1"
    )
    
    # Question 2
    q2 = st.radio(
        "2. Which account category does Cash belong to?",
        options=[
            "Please select",
            "Assets",
            "Liabilities",
            "Equity",
            "Revenue",
            "Expenses"
        ],
        key="q2"
    )
    
    # Question 3
    q3 = st.radio(
        "3. What is the fundamental equation of the Balance Sheet?",
        options=[
            "Please select",
            "Assets = Liabilities + Equity",
            "Assets = Liabilities - Equity",
            "Assets + Liabilities = Equity"
        ],
        key="q3"
    )
    
    # Question 4
    q4 = st.radio(
        "4. Which financial statement shows a company’s profitability over a period?",
        options=[
            "Please select",
            "Income Statement",
            "Balance Sheet",
            "Cash Flow Statement"
        ],
        key="q4"
    )
    
    # Question 5
    q5 = st.radio(
        "5. What does a journal entry do?",
        options=[
            "Please select",
            "Records a transaction with debits and credits",
            "Calculates net income",
            "Provides an annual summary"
        ],
        key="q5"
    )
    
    # Question 6
    q6 = st.radio(
        "6. In accrual accounting, when is revenue recognized?",
        options=[
            "Please select",
            "When earned",
            "When cash is received",
            "When the invoice is issued",
            "When the contract is signed"
        ],
        key="q6"
    )
    
    # Question 7
    q7 = st.radio(
        "7. What is a reversing entry?",
        options=[
            "Please select",
            "An entry that cancels a previous accrual",
            "An entry that adjusts inventory",
            "An entry that records depreciation"
        ],
        key="q7"
    )
    
    # Question 8
    q8 = st.radio(
        "8. What effect does recording an accrual have on the financial statements?",
        options=[
            "Please select",
            "Increases expenses and increases liabilities",
            "Increases expenses and increases assets",
            "Increases revenue and increases liabilities"
        ],
        key="q8"
    )
    
    # Question 9
    q9 = st.radio(
        "9. What happens to net income when expenses exceed revenue?",
        options=[
            "Please select",
            "Net loss",
            "Net income is positive",
            "No effect"
        ],
        key="q9"
    )
    
    # Question 10
    q10 = st.radio(
        "10. What is the purpose of the Chart of Accounts?",
        options=[
            "Please select",
            "To organize all accounts used by a company",
            "To record individual transactions",
            "To prepare bank reconciliations"
        ],
        key="q10"
    )
    
    if st.button("Submit Final Quiz", key="submit_final_quiz"):
        # Define correct answers
        correct_answers = {
            "q1": "Balance Sheet, Income Statement, Cash Flow Statement",
            "q2": "Assets",
            "q3": "Assets = Liabilities + Equity",
            "q4": "Income Statement",
            "q5": "Records a transaction with debits and credits",
            "q6": "When earned",
            "q7": "An entry that cancels a previous accrual",
            "q8": "Increases expenses and increases liabilities",
            "q9": "Net loss",
            "q10": "To organize all accounts used by a company"
        }
        
        user_answers = {
            "q1": q1,
            "q2": q2,
            "q3": q3,
            "q4": q4,
            "q5": q5,
            "q6": q6,
            "q7": q7,
            "q8": q8,
            "q9": q9,
            "q10": q10,
        }
        
        results = []
        score = 0
        for q, correct in correct_answers.items():
            user_ans = user_answers[q]
            is_correct = (user_ans == correct)
            if is_correct:
                score += 1
            results.append({
                "Question": q,
                "Your Answer": user_ans,
                "Correct Answer": correct,
                "Result": "Correct" if is_correct else "Incorrect"
            })
        
        result_df = pd.DataFrame(results)
        st.markdown("### Quiz Results")
        st.table(result_df)
        st.markdown(f"**Total Score: {score} out of 10**")

if __name__ == '__main__':
    main()
