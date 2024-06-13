$(document).ready(function () {
	// 유효성검사 통과 여부
	let isUsernameValid = false;
	let isNicknameValid = false;
	let isPasswordValid = false;

	function toggleSubmitButton() {
		if (isUsernameValid && isNicknameValid && isPasswordValid) {
			$('#loginBtn').prop('disabled', false);
		} else {
			$('#loginBtn').prop('disabled', true);
		}
	}

	$('#registerBtn').on('click', function () {
		if (
			confirm('회원가입을 취소할까요?\n입력된 정보는 저장되지 않습니다.') ==
			true
		) {
			window.location.href = '../login';
		} else {
			//취소
			return false;
		}
	});

	// Username 중복 검사
	$("input[name='username']").on('keyup', function () {
		const username = $(this).val();
		$.ajax({
			type: 'POST',
			url: checkUsernameUrl,
			contentType: 'application/json',
			data: JSON.stringify({ username: username }),
			success: function (response) {
				if (response.exists) {
					$("input[name='username']").css('border-color', '#ff0000');
					isUsernameValid = false;
				} else {
					$("input[name='username']").css('border-color', '#138900');
					isUsernameValid = true;
				}
				toggleSubmitButton();
			},
		});
	});

	// Nickname 중복 검사
	$("input[name='nickname']").on('keyup', function () {
		const nickname = $(this).val();
		$.ajax({
			type: 'POST',
			url: checkNicknameUrl,
			contentType: 'application/json',
			data: JSON.stringify({ nickname: nickname }),
			success: function (response) {
				if (response.exists) {
					$("input[name='nickname']").css('border-color', '#ff0000');
					isNicknameValid = false;
				} else {
					$("input[name='nickname']").css('border-color', '#138900');
					isNicknameValid = true;
				}
				toggleSubmitButton();
			},
		});
	});

	// password 유효성 검사
	$("input[name='confirm_password'], input[name='password']").on(
		'keyup',
		function () {
			const password = $("input[name='password']").val();
			const confirmPassword = $("input[name='confirm_password']").val();
			if (password === confirmPassword && password !== '') {
				$("input[name='confirm_password']").css('border-color', '#138900');
				isPasswordValid = true;
			} else {
				$("input[name='confirm_password']").css('border-color', '#ff0000');
				isPasswordValid = false;
			}
			toggleSubmitButton();
		}
	);

	// 초기 버튼 비활성화
	$('#loginBtn').prop('disabled', true);
});
