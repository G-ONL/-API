var xhr = new XMLHttpRequest();

// TODO URL 기반 상품 조회 API 적용
var url = 'http://localhost:8080/api/product?productUrl=';

chrome.tabs.executeScript({
    code: 'window.location.href;'
}, function (result) {
    xhr.open('GET', url + result[0]);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var data = xhr.responseText;
            var jsonParseData = JSON.parse(data);
            console.log(jsonParseData);

            if (jsonParseData.response.msg == 'Product Not Exist') {
                alert("상품이 존재하지 않습니다.");
            } else {
                var productInfo = jsonParseData.response.data;
                var productPrice = productInfo.productPrice;

                var paymentTypes = jsonParseData.paymentTypes;

                // 상품명
                document.querySelector('#productName').value = productInfo.productName;
                // 상품 가격
                document.querySelector('#productPrice').value = productPrice;
                // 결제 수단
                for (let i = 0; i < paymentTypes.length; ++i) {
                    console.log(paymentTypes[i]);
                    var select = document.getElementById('paymentTypes');
                    var option = document.createElement('option');
                    option.setAttribute('name', paymentTypes[i]);
                    option.textContent = paymentTypes[i];
                    select.appendChild(option);
                }
            }
        }
    };
    xhr.send();
});
