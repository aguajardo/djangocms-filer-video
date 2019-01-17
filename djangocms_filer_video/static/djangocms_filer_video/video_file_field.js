django.jQuery(function ($) {

    var dropzoneSelector = '.js-filer-dropzone';
    $(dropzoneSelector).each(function (idx, el) {
        var dropzone = el.dropzone;
        var $input = $(el).find('.adminVideoFileWidget');
        if ($input) {
            dropzone.options.maxFilesize = 5000;
            
            var defaultUploadUrl = $input.data('default-upload-url');
            if (defaultUploadUrl) {
                dropzone.options.url = defaultUploadUrl;
            }

            dropzone.on("success", function (file, response) {
                if (file && file.status === 'success' && response) {
                    if (response.thumbnail) {
                        $('.dz-thumbnail img').attr('src', response.thumbnail);
                    }
                }
            });
        }
    });

});