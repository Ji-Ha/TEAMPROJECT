document.addEventListener("DOMContentLoaded", function() {
  // downloadInnerHtml(".CommentsPanel-scrollable--HblrE", 'text/csv');
  downloadInnerHtml();

  chrome.extension.sendMessage({
      action: "getSource",
      source: get_source(document.body)
  });

});

function get_source(document_body){
    return document_body.innerText;
}

chrome.extension.sendMessage({
    action: "getSource",
    source: get_source(document.body)
});
function downloadInnerHtml() {

  var data = "id,comment_text\n";
  var sample = "id,toxic,severe_toxic,obscene,threat,insult,identity_hate\n"
  // var len = elHtml.match(/"Comment-commentText--1826c"/g);
  var obj = document.getElementsByClassName("Comment-commentText--1826c");

  for (let i = 0; i < obj.length; i++) {
    // var temp = $(obj.item(i)).text();
    var temp = obj[i].firstChild.nodeValue;
    if (temp) {
      temp = temp.replace(/,/gi, "");
      temp = temp.replace(/\n/gi, " ");
    }
    data += (i + 1) + ", " + temp + "\n";
    sample += (i + 1) + ", 0.5,0.5,0.5,0.5,0.5,0.5\n"
  }


  var linkReply = document.createElement('a');
  linkReply.setAttribute('download', 'reply.csv');
  linkReply.setAttribute('href', 'data:data:text/csv; charset=utf-8,' + data);

  linkReply.click();
  setTimeout(function() {
    linkReply.setAttribute('download', 'sample_submission.csv');
    // linkReply.setAttribute('href', 'data:' + mimeType + '; charset=utf-8,' + sample);
    linkReply.setAttribute('href', 'data:text/csv; charset=utf-8,' + sample);
    linkReply.click();
  })

}



// $(document).ready(function() {
//   downloadInnerHtml(".CommentsPanel-scrollable--HblrE", 'text/csv');
//
// });
