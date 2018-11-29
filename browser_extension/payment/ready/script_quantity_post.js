function paymentRequest(quantity) {
    var xhr = new XMLHttpRequest();
    // TODO 임시 URL (결제 요청 API?)
    var url = 'https://www.gitflow.org/api/login';  // 임시
    xhr.open('POST', url);

    var jsonModel = '{ "login" : "mingooddev", "password" : "qmdkthf587" }'; // 임시
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            console.log(quantity);

            var data = xhr.responseText;
            console.log(data);
            var jsonResponseText = JSON.parse(data);

            if (jsonResponseText.msg == 'Login Success') {
                // next 라는 id 를 갖는 div 태그를 찾는다.
                var div = document.getElementById('next');
                // a tag 를 생성한다.
                var link = document.createElement('a');
                // 생성한 a tag 의 href 속성 추가
                link.setAttribute('href', '/payment/request/popup_payment_request.html');
                // textContent 를 추가
                link.textContent = 'NEXT';
                // div tag 의 자식으로 a tag 를 삽입
                div.appendChild(link);
            }
        }
    };

    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(jsonModel);    // 임시
}

var action = document.getElementById('submit');
action.addEventListener('click', function () {
    var quantity = document.querySelector('#quantity').value;
    paymentRequest(quantity);
});