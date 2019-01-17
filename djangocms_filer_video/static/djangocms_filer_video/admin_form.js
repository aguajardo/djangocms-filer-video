(function ($) {
    $(function () {
        window.DjangoFilerVideo = {
            retryConversion: function (element) {
                var $element = $(element);
                var url = $element.data('url');
                $.ajax({
                    url: url,
                    success: function (data) {
                        $element.parent().html(data.status);
                    }
                });
            },
            updateStatuses: function () {
                $('.field-status_action [data-refresh-url]').each(function (index, element) {
                    var $element = $(element);
                    var url = $element.data('refresh-url');
                    $.ajax({
                        url: url,
                        success: function (data) {
                            $element.parent().html(data.status_admin_action);
                        }
                    });
                });
            }
        };

        var updateIntervalID = setInterval(
            window.DjangoFilerVideo.updateStatuses,
            5000
        );
    });
})(django.jQuery);