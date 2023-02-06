
def condition(s):
        if ((s['R_rank']=="2") or (s['R_rank']=="1")) and (s['F_rank']=="5"):
            return "Cant Lose Them"
        elif ((s['R_rank']=="2") or (s['R_rank']=="1")) and  ((s['F_rank']=="4") or  (s['F_rank']=="3")):
            return "At Risk"
        elif ((s['R_rank']=="2") or (s['R_rank']=="1")) and ((s['F_rank']=="2") or  (s['F_rank']=="1")):
            return "Hibernatting"
        elif (s['R_rank']=="3") and ((s['F_rank']=="2") or  (s['F_rank']=="1")):
            return "About to Sleep"
        elif (s['R_rank']=="3") and (s['F_rank']=="3"):
            return "Need Attention"
        elif ((s['R_rank']=="3") or  (s['R_rank']=="4"))  and ((s['F_rank']=="4") or  (s['F_rank']=="5")):
            return "Loyal User"
        elif  (s['R_rank']=="4") and (s['F_rank']=="1"):
            return "Promising"
        elif  (s['R_rank']=="5") and (s['F_rank']=="1"):
            return "Flash Customer" ###replace new customer van dang tim cai ten goi khac cho class nay, do neu su dung transition voi 2 khoang thang khac nhau,vi du thang 9 voiw thang 10, neu 1 class champions cua thang 9 chuyen thanh class flash customer hay new customer thi se khong hop ly lam
        elif ((s['R_rank']=="4") or (s['R_rank']=="5")) and ((s['F_rank']=="2") or  (s['F_rank']=="3")):
            return "Potentital Loyalist"
        elif  (s['R_rank']=="5") and ((s['F_rank']=="4") or  (s['F_rank']=="5")):
            return "Champions"
        else:
            return "Others" 