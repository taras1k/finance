$(function(){
    ko.extenders.required = function(target, overrideMessage) {
        //add some sub-observables to our observable
        target.hasError = ko.observable();
        target.validationMessages = ko.observableArray();

        //define a function to do validation
        function validate(newValue) {
           target.hasError(newValue ? false : true);
           var validationMessage = overrideMessage || "This field is required";
           target.validationMessages.remove(validationMessage);
           if(!newValue){
               target.validationMessages.push(validationMessage);
           }
        }

        //initial validation
        validate(target());

        //validate whenever the value changes
        target.subscribe(validate);

        //return the original observable
        return target;
    };
    var expenseViewModel = {
        expenseAmount: ko.observable().extend({required: 'Please input'}),
        expenseCurrency: ko.observable(),
        save: function(){
            console.log(this.expenseAmount.validationMessages())
            this.expenseAmount.validationMessages.remove('sasa');
            this.expenseAmount.validationMessages.push('sasa');
        }
    };
    var expense_input = document.getElementById('expense_input');
    ko.applyBindings(expenseViewModel, expense_input);
});
