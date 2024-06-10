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
});

$('#createBtn').on('click', function () {
	alert('준비 중인 기능입니다.');
});
