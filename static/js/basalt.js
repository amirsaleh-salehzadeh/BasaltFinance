var tweenMenuShow

function populateWarningMessageField(fieldId, text) {
	var errorSection = $("<small/>").addClass("text-warning")
	$("<br/>").appendTo(errorSection)
	errorSection.append(text)
	$("#" + fieldId).parent().find("label").after(errorSection)
}

function populateDangerMessageField(fieldId, text) {
	$("small." + fieldId).remove()
	var errorSection = $("<small/>").addClass("text-danger " + fieldId)
	$("<br/>").appendTo(errorSection)
	errorSection.append(text)
	$("#" + fieldId).before(errorSection)
}

// FOR MANY FIELDS
function populateErrorMessageFields(errorString) {
	Object.keys(JSON.parse(errorString)).forEach(function(key, value) {
		var errorSection = $("<small/>").addClass("text-danger")
		$("<br/>").appendTo(errorSection)
		errorSection.append(JSON.parse(errorString)[key][0].message)
		$("#" + key).after(errorSection)
	})
}

function openFullScreenDiv(htmlContenet) {
	$(".full-screen-div").html(htmlContenet)
	$(".full-screen-div").css("display", "block")
	$(this).find(".close-button").load('static/img/icons/close.svg')
	$(".dialog-popup-content").append(
			$("<div/>").addClass("close-button").attr("onclick",
					"closeFullScreenDiv()"))
	TweenLite.to(".full-screen-div", .333, {
		scale : 1,
		top : 0,
		right : 0,
		left : 0,
		bottom : 0,
		transformOrigin : "center"
	})
}

function closeFullScreenDiv() {
	TweenLite.to(".full-screen-div", .333, {
		scale : 0,
		transformOrigin : "center",
		onComplete : function() {
			$(".full-screen-div").html("")
		}

	})
}

function loadContent(liItem) {
alert(liItem)
	$(".navbar-collapse").removeClass("show")
	$("div#page-content").hide()
	$("#banner-bottom-1").fadeIn()
	$(".frameLoding").fadeIn()
	var url = ""
	$(".menu-item").removeClass("active")
	$(liItem).addClass("active")
	url = $(liItem).attr("data-href")
	$(".page-content-area-bg").remove()
	$(".page-content-area").remove()
	$.ajax({
		url : url,
		cache : false,
		success : function(response) {
			var tl = new TimelineLite({
				paused : true,
				ease : Power4.easeOut
			})
			tl.to("#page-content", 1, {
				opacity : 0
			}).to("#page-content", 1.2, {
				opacity : 1
			}, "-= .4")
			$("#page-content").fadeIn()
			$("#page-content").html("")
			$(".page-content-holder").prepend(
					$("<div/>").addClass("page-bg-svg"))
			$(".page-bg-svg").find("span").remove()
			$("#page-content").prepend(
					$("<div/>").addClass("page-content-area"))
			$(".page-content-area").html(response)
			convertImg2SVG("svgNonMenu")
			$("#page-content").prepend(
					$("<div/>").addClass("page-content-area-bg"))
			$(".page-content-area-bg").html(
					$(".menu-item.active").find("a").html())
			$(".banners-background-image").css(
					"background-position",
					Math.floor(Math.random() * 333) + "px "
							+ Math.floor(Math.random() * 333) + "px")
			tl.play()
			if ($(liItem).attr("data-color") != null) {
				var color = "var(" + $(liItem).attr("data-color") + ")";
				$("#banner-top").css("background-color",
						"var(" + $(liItem).attr("data-color") + ")")
			}
			$(".frameLoding").fadeOut()
		}
	})
}

$(document).ready(function() {
	TweenLite.to(".full-screen-div", .333, {
		scale : 0,
		transformOrigin : "center"
	})

})


// SHOWS/HIDES THE MESSAGE BOX,
// INPUT: 1- gets a text message and boolean (True pops the error message. False
// pops the success message)
function toggleMessageBox(messageText, isError) {
	if (isError) {
		$(".error-message-content").html(messageText)
		$("#error-message-modal").modal("show")
	} else {
		$(".success-message-content").html(messageText)
		$("#success-message-modal").modal("show")
	}
}

function toggleConfirmationBox(callback) {
	$(".confirmation-message-content").html(arguments[1])
	$("#confirmation-box-modal").modal("show")
	const args = [].slice.call(arguments)
	$("#confirmation-box-btn").unbind( "click" );
	$("#confirmation-box-btn").on("click",function() {
		callback(args)
		$("#confirmation-box-modal").modal("hide")
	})
}

function showDialogPage(element, url) {
	$("<div/>").load(
			url,
			function(response) {
				openFullScreenDiv("<div class='dialog-popup-content'>"
						+ response + "</div>")
			})
	return -1
}

function getCookie(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie != '') {
		var cookies = document.cookie.split(';');
		for (var i = 0; i < cookies.length; i++) {
			var cookie = $.trim(cookies[i]);
			if (cookie.substring(0, name.length + 1) == (name + '=')) {
				cookieValue = decodeURIComponent(cookie
						.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}

function submitAnEvaluationForm() {
	var url = arguments[0][2], formId = arguments[0][3], submitBTNId = arguments[0][4], newStatus = arguments[0][5]
	if (newStatus != null)
		$('#' + formId).find('#statusfield').val(newStatus)
	var form = $('#' + formId)[0]
	$("#" + submitBTNId).prop("disabled", true)
	var data = new FormData(form)
	$.ajax({
		type : "POST",
		data : data,
		processData : false,
		contentType : false,
		cache : false,
		url : url,
		beforeSend : function(xhr, settings) {
			if (!(/^http:.*/.test(settings.url) || /^https:.*/
					.test(settings.url))) {
				xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
			}
		},
		success : function(response) {
			if (response.successResult != null) {
				toggleMessageBox(response.successResult, false)
				$('#admin-console-content').load('/work_lists?status=-2')
				closeFullScreenDiv()
			} else if (response.errorResults != null) {
				populateErrorMessageFields(response.errorResults)
			} else if (response.errorResult != null)
				toggleMessageBox("<span>" + response.errorResult + "</span>",
						true)
		},
		error : function(xhr, errmsg, err) {
			console.log(xhr.status + ": " + xhr.responseText)
			toggleMessageBox(xhr.responseText, true)
		},
		complete : function(response) {
			$("#" + submitBTNId).prop("disabled", false)
			return -1
		}
	})
}

function loginForm(url, formId, submitBTNId) {
	var form = $('#' + formId)[0]
	$("#" + submitBTNId).prop("disabled", true)
	var data = new FormData(form)
	$.ajax({
		type : "POST",
		data : data,
		processData : false,
		contentType : false,
		cache : false,
		url : url,
		beforeSend : function(xhr, settings) {
			if (!(/^http:.*/.test(settings.url) || /^https:.*/
					.test(settings.url))) {
				xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
			}
		},
		success : function(response) {
			if (response.successResult != null) {
				toggleMessageBox(response.successResult, false)
			} else if (response.errorResults != null) {
				populateErrorMessageFields(response.errorResults)
			} else if (response.errorResult != null)
				toggleMessageBox("<span>" + response.errorResult + "</span>",
						true)
			else {
				$("#login-div").load('/user/login/')
			}
		},
		error : function(xhr, errmsg, err) {
			console.log(xhr.status + ": " + xhr.responseText)
			toggleMessageBox(xhr.responseText, true)
		},
		complete : function(response) {
			$("#" + submitBTNId).prop("disabled", false)
			return -1
		}
	})
}
