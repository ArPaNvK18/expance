from django.http import HttpResponse
from django.shortcuts import render
from .models import AddAll


def index(request):
    # Fetch data from HTML and save in DB
    if request.method == 'POST':
        Payment_Type = request.POST['pt']
        Transaction_Type = request.POST['tt']
        Rs = request.POST['rs']
        Comment = request.POST['comment']
        Date = request.POST['date']
        print(Payment_Type,Transaction_Type,Rs,Comment,Date)

        save_data = AddAll(Payment_Type=Payment_Type,Transaction_Type=Transaction_Type,Rs=Rs,Comment=Comment,Date=Date)
        save_data.save()

    # fetch data from DB
    all_data = AddAll.objects.all()

    # Calculate expence
    total_spend = 0
    for i in all_data:
        # print(i.Rs,i.Transaction_Type)
        if (i.Transaction_Type == 'Debit'):
            total_spend = total_spend+int(i.Rs)
            print(total_spend)
        elif(i.Transaction_Type == 'Credit'):
            total_spend = total_spend-int(i.Rs)
            print(total_spend)
    params = {'all_data':all_data,'total_spend':total_spend}
    return render(request,'index.html',params)

def transaction(request):
    all_data = AddAll.objects.all()
    return render(request,'index.html',{'all_data':all_data})