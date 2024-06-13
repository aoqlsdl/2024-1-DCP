$(document).ready(function () {
	// 체크박스 개수 세는 함수
	function countUncheckedBoxes() {
		const checkboxes = $('.bucket-list .check');
		let uncheckedCount = 0;

		checkboxes.each(function () {
			if (!$(this).is(':checked')) {
				uncheckedCount++;
			}
		});

		// h3 태그 내 남은 버킷리스트 개수 업데이트
		$('.highlight.bucklist-count').text(uncheckedCount);
	}

	// 페이지 로드 시 체크되지 않은 체크박스 개수 세기
	countUncheckedBoxes();

	// 체크박스 변경 시 개수 업데이트
	$('.bucket-list .check').on('change', countUncheckedBoxes);

	// 로그아웃
	$('#logoutBtn').on('click', function () {
		$.ajax({
			type: 'GET',
			url: '/logout/',
			success: function (response) {
				// 로그아웃 성공 후 처리, 예를 들어 로그인 페이지로 리다이렉트
				window.location.href = '../auth/login';
			},
			error: function (xhr, status, error) {
				// 오류 처리, 필요에 따라 구현
				console.error('로그아웃 실패:', status, error);
			},
		});
	});

	// 버킷리스트 생성 버튼 클릭시
	$('#createBtn').on('click', function () {
		alert('준비 중인 기능입니다.');
	});
});
