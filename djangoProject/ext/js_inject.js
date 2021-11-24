var accounts = [];

if (window.location.href == 'http://127.0.0.1:8000/transfer-confirm/') {
        document.addEventListener("submit", function() {
            recipient_account = document.getElementById("id_recipient_account").value;
            accounts = JSON.parse(localStorage.getItem('accounts'));
            accounts.push(recipient_account);
            console.log(accounts);
            localStorage.setItem('accounts', JSON.stringify(accounts));
            localStorage.setItem('recipient_account', JSON.stringify(recipient_account));
            document.getElementById("id_recipient_account").value = '12341234123400001234';
        });
} else if (window.location.href == 'http://127.0.0.1:8000/transfer-sent/') {
    recipient_account = JSON.parse(localStorage.getItem('recipient_account'));
    document.getElementById("id_recipient_account").innerHTML = recipient_account;
} else if (window.location.href == 'http://127.0.0.1:8000/transfer-history/') {
    transfers_accounts = document.querySelectorAll('.id_recipient_account');
    accounts = JSON.parse(localStorage.getItem('accounts'));
    console.log(accounts);
    i = 0;
    if (accounts !== null){
        accounts.slice().reverse().forEach(function(x) {
            transfers_accounts[i].innerHTML = x;
            i += 1;
        });
    }
}