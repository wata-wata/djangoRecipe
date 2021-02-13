$(function() {
  // チェックボックスのクリックを無効化します。
  $('.image_box .disabled_checkbox').click(function() {
    return false;
  });

  // 画像がクリックされた時の処理です。
  $('img.thumbnail').on('click', function() {
    if (!$(this).is('.checked')) {
      // チェックが入っていない画像をクリックした場合、チェックを入れます。
      $(this).addClass('checked');
    } else {
      // チェックが入っている画像をクリックした場合、チェックを外します。
      $(this).removeClass('checked')
    }
  });
});