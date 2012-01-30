$(document).ready(function() {
  $('.search_form').validate({
    focusInvalid: true,
    errorPlacement: function(label, element){
      false;
    }
  });
  $('#searchGadget').rules('add', {
      required: true,
  });
});
