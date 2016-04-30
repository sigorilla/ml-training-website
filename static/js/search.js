(function () {

$(document).ready(init);

function init() {
    new Search();
}

var TIMER = 2000;

function Search() {
    this._$input = $('.search-input');
    this._$preview = $('.search-preview');
    this._timer = null;

    this._addEventListeners();
}

Search.prototype = {
    /**
     * Добавляем события.
     */
    _addEventListeners: function () {
        this._$input.on({
            focus: this._onChangeQuery.bind(this),
            input: this._onChangeQuery.bind(this),
            blur: this._setTimer.bind(this)
        });
        this._$preview.on({
            mouseenter: this._unsetTimer.bind(this),
            mouseleave: this._setTimer.bind(this)
        });
    },

    /**
     * Обработчик изменения текста в поле поиска.
     */
    _onChangeQuery: function () {
        var q = $.trim(this._$input.val());
        if (q) {
            var query = this._$input.parents('form').attr('action') + '?q=' + encodeURIComponent(q);
            this._$preview.find('.popover-content').html('&nbsp;').load(query, function () {
                this._unsetTimer();
                this._$preview.show();
            }.bind(this));
        }
    },

    _setTimer: function () {
        if (!this._timer && !this._$input.is(':focus')) {
            this._timer = window.setTimeout(this._hidePreview.bind(this), TIMER);
        }
    },

    _unsetTimer: function () {
        if (this._timer) {
            window.clearTimeout(this._timer);
            this._timer = null;
        }
    },

    _hidePreview: function () {
        this._$preview.hide();
    }
};

})();
