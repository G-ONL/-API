function sendUserInfo(email, phone) {
    // TODO API 에서 받는 모델에 따라 변경해야함
    var jsonModel = '{ "email" : "' + email + '", "phone" : "' + phone + '" }';

    var xhr = new XMLHttpRequest();
    // var url = 'https://www.gitflow.org/api/login';
    var url = 'http://localhost:8080/api/login';
    xhr.open('POST', url);

    /**
     * onreadystatechange: 서버와의 통신이 끝났을 때 호출되는 이벤트
     * readyState: 통신의 현재 상태 (4: 통신 완료를 의미)
     * status: HTTP 통신의 결과를 의미 (200: 성공)
     * responseText 는 서버에서 전송한 데이터
     */
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var data = xhr.responseText;
            var jsonResponseText = JSON.parse(data);

            console.log(jsonResponseText);
            console.log(jsonResponseText.msg);

            if (jsonResponseText.msg == 'Login Success') {
                // next 라는 id 를 갖는 div 태그를 찾는다.
                var div = document.getElementById('next');
                // a tag 를 생성한다.
                var link = document.createElement('a');
                // 생성한 a tag 의 href 속성 추가
                link.setAttribute('href', '/payment/ready/popup_payment_ready.html');
                // textContent 를 추가
                link.textContent = 'NEXT';
                // div tag 의 자식으로 a tag 를 삽입
                div.appendChild(link);
            } else {
                // TODO response msg 에 따라 email, password 각각 틀린 정보를 체크하여 더 분기 처리 가능
                alert("잘못된 정보를 입력하셨습니다.");
            }
        }
    };

    // 서버로 전송할 데이터 타입의 형식 지정
    xhr.setRequestHeader("Content-Type", "application/json");
    // send 메소드의 파라미터를 활용하여 전송할 데이터를 전달
    xhr.send(jsonModel);

    // 헤더를 찾아보자
    // var headers = xhr.getAllResponseHeaders();
    // console.log(headers);
}

var action = document.getElementById('submit');
action.addEventListener('click', function () {
    var email = document.querySelector('#email').value;
    var phone = document.querySelector('#phone').value;

    sendUserInfo(email, phone);
});