$(document).ready(function () {
	$('#loginForm').on('submit', function (event) {
		event.preventDefault(); // 기본 폼 제출 동작 막기
		const formData = {
			username: $("input[name='username']").val(),
			password: $("input[name='password']").val(),
			csrf_token: $("input[name='csrf_token']").val(),
		};
		$.ajax({
			type: 'POST',
			url: loginUrl,
			contentType: 'application/json',
			data: JSON.stringify(formData),
			success: function (response) {
				if (response.success) {
					window.location.href = mainIndexUrl; // 로그인 성공 시 리다이렉션
				} else {
					alert(response.message); // 오류 메시지 표시
					console.log(response);
				}
			},
			error: function () {
				alert('서버에서 오류가 발생했습니다. 잠시 후 다시 시도해주세요.');
			},
		});
	});
});
