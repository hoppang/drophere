"use strict";

var manualUpload = document.querySelector('#manualUpload');
var progressBar = document.querySelector('#progressBar');
var dropzone = document.querySelector('#dropzone');
var result = document.querySelector('#result');

dropzone.addEventListener("dragover", dragOverHandler, false);
dropzone.addEventListener("dragleave", dragLeaveHandler, false);
dropzone.addEventListener("drop", dropHandler, false);

manualUpload.onchange = function () {
	uploadFile(manualUpload.files[0]);
};

function dropHandler(evt) {
	evt.stopPropagation();
	evt.preventDefault();
	result.innerText = "";
	uploadFile(evt.dataTransfer.files[0]);
}

function dragOverHandler(evt) {
	evt.stopPropagation();
	evt.preventDefault();
}

function dragLeaveHandler(evt) {
	console.log('drag leave');
	evt.stopPropagation();
	evt.preventDefault();
}

function uploadFile(file) {
	var formData = new FormData();
	formData.append("file", file);

	var xhr = new XMLHttpRequest();
	xhr.open('POST', '', true);
	xhr.upload.addEventListener('progress', updateProgress, false)
	xhr.onload = function() {
		console.log(this.responseText);
	};
	xhr.onloadend = function() {
		result.innerText = "upload complete";
		console.log("upload complete");
	}

	xhr.send(formData);
}

function updateProgress(evt) {
	console.log("progress:", evt.loaded, "/", evt.total);
	progressBar.value = evt.loaded;
	progressBar.max = evt.total;
}
