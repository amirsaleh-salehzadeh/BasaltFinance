var totalFields = 0
var filledFields = 0
var questionsValidated = 0;
function submitRegistryForm(url) {
	var form = $('#registry-form')[0]
	$("#register-btn").prop("disabled", true)
	var data = new FormData(form)
	$
			.ajax({
				type : "POST",
				enctype : 'multipart/form-data',
				data : data,
				processData : false,
				contentType : false,
				cache : false,
				timeout : 60000,
				url : url,
				beforeSend : function(xhr, settings) {
					$(".frameLoding").fadeIn()
					if (!(/^http:.*/.test(settings.url) || /^https:.*/
							.test(settings.url))) {
						xhr.setRequestHeader("X-CSRFToken",
								getCookie('csrftoken'))
					}
				},
				success : function(response) {
					if (response.successResult != null) {
						toggleMessageBox(response.successResult, false)
					} else if (response.errorResults != null) {
						populateErrorMessageFields(response.errorResults, true)
					}
				},
				error : function(xhr, errmsg, err) {
					console.log(xhr.status + ": " + xhr.responseText)
					toggleMessageBox(xhr.responseText, true)
				},
				complete : function(response) {
					$("#register-btn").prop("disabled", false);
					$(".frameLoding").fadeOut()
					return -1
				}
			})
}

