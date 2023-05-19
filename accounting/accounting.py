import sys
import user.authentication
import transactions.journal
import banking.reconciliation
# import banking.fvb.reconciliation
# import banking.ubsa.reconciliation
# import banking.online.reconciliation

if __name__ == "__main__":
    # if len(sys.argv) > 1:
    for thing in sys.argv[1::]:
        print(thing)

    user.authentication.authenticate_user()

    transactions.journal.receive_income(100.00)
    transactions.journal.pay_expense(100.00)

    banking.reconciliation.do_reconciliation()    
    banking.fvb.reconciliation.do_reconciliation()
    banking.ubsa.reconciliation.do_reconciliation()
    banking.online.reconciliation.do_reconciliation()
    help("modules")

    

    

