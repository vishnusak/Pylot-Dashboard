$(document).ready(function(){
  $('.cmt').hide()
  showcomments()

  $('.post_msg').submit(function(e){
    e.preventDefault()
    var for_id = this.id
    var form_data = $(this).serialize()
    $.ajax({
      type: 'post',
      url: '/messages/'+for_id,
      data: form_data,
      success: function(resp){
        $('.bottom').html(resp)
        $('.cmt').hide()
        showcomments()
        $('.post_msg').trigger('reset')
      }
    })
  })
})

function showcomments(){
  $('.msg-body').on('click', 'button', function(){
    var msg_id = this.id
    var cmt_block_id = 'cmt'+msg_id
    if ($('#'+cmt_block_id).is(':hidden')){
      $.ajax({
        type: 'post',
        url: '/messages/get_comments/'+msg_id,
        success: function(resp){
          $('#cblock'+msg_id).html(resp)
        }
      })
      $('#'+cmt_block_id).show()
    } else {
      $('#'+cmt_block_id).hide()
    }
  })

  $('.post_cmt').submit(function(e){
    e.preventDefault()
    var msg_id = this.id
    var cmt_block_id = 'cmt'+msg_id
    var form_data = $(this).serialize()
    $.ajax({
      method: 'post',
      url: '/comments/'+msg_id,
      data: form_data,
      success: function(resp){
        $('#cblock'+msg_id).html(resp)
        $('.post_cmt').trigger('reset')
      }
    })
  })

}
