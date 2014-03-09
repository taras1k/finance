$(function(){
    var ListExpenseViewModel = function() {
        var self = this;
        self.transactions = ko.observableArray();
        self.get_transactions = function(){
            $.ajax({
                method: 'GET',
                url: '/api/transaction/',
            }).done(function(data){
                data['objects'].forEach(function(obj){
                    self.transactions.push({
                        id: ko.observable(obj.id),
                        amount: ko.observable(obj.amount)
                    });
                });
            });
        };
    };
    var AddExpenseViewModel = function() {
        var self = this;
        self.expenseAmount = ko.observable(10);
        self.expenseAmountError = ko.observable();
        self.expenseCurrency = ko.observable();
        self.save = function(){
            self.expenseAmountError('');
            data = {
                'amount': self.expenseAmount()
            }
            $.ajax({
                method: 'POST',
                url: '/api/transaction/',
                data: ko.toJSON(data),
                dataType: 'json',
                contentType: 'application/json'
            }).done(function(data){
                console.log(data);
            }).fail(function(error){
                var errors = $.parseJSON(error.responseText);
                if('amount' in errors){
                    self.expenseAmountError(errors.amount);
                }
            });
        }
    };

    var addExpenseViewModel = new AddExpenseViewModel();
    var listExpenseViewModel = new ListExpenseViewModel()
    listExpenseViewModel.get_transactions();
    var ViewModel = function(){
        var self = this;
        self.crete_transaction = addExpenseViewModel;
        self.list_transaction = listExpenseViewModel;
    };
    var viewModel = new ViewModel();
    ko.applyBindings(viewModel);
});
