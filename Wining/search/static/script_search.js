
 $(document).ready(
	function() {

		var searchnameerror = "검색어를 입력하세요.";
		var searcherror = "검색에 실패했습니다\n잠시 후 다시 시도하세요";
		var alcoholerror = "작은 값과 큰 값을 순서대로 입력하세요."
		

		function erroralert( msg ) {
			alert( msg );
			history.back();
		}
		
		
		// 이름 검색
		$("form[name='searchbyname']").on(
			"submit",
			function(event) {
				if(! $("input[name='searchname']").val()) {
					alert(searchnameerror);
					$("input[name='searchname']").focus();
					return false;
				} 
			}	
		);
	
		// 도수 입력 
		$("form[name='searchbycategory']").on(
			"submit",
			function(event) {
				if($("input[name='alcmin']").val() > $("input[name='alcmax']").val()) {
					alert(alcoholerror);
					$("input[name='alcmin']").focus();
					return false;
				} 
			}	
		);
/*		
		
		// 글수정
		$("form[name='updateform']").on(
			"submit",	
			function ( event ) {
				if( ! $("input[name='subject']").val() ) {
					alert( subjecterror );
					updateform.subject.focus();
					return false;
				} else if( ! $("textarea[name='content']").val() ) {
					alert( contenterror );
					updateform.content.focus();
					return false;
				} else if( ! $("input[name='passwd']").val() ) {
					alert( passwderror );
					updateform.passwd.focus();
					return false;
				}
			}
		);
		

*/
	
	} // function
); // ready
		
