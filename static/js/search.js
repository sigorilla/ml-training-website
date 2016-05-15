(function () {

$(document).ready(init);

function init() {
    new Search();
}

var TIMER = 2000;

function Search() {
    this._$input = $('.search-input');
    this._$preview = $('.search-preview');
    this._$checkbox = $('.search-form .dropdown-menu a[data-type = checkbox]');
    this._timer = null;

    this._parseSearch();
    this._addEventListeners();
}

Search.prototype = {
    _parseSearch: function () {
        var search = location.search.slice(1);
        search.split('&').forEach(function (param) {
            var data = param.split('=');
            if (data[0] === 'actual') {
                this._changeCheckbox(this._$checkbox.filter('.for-actual'));
            }
        }.bind(this));
    },

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
        this._$checkbox.on({
            click: this._onCheckboxClick.bind(this)
        });
    },

    /**
     * Обработчик изменения текста в поле поиска.
     */
    _onChangeQuery: function () {
        var $form = this._$input.parents('form');
        var q = $.trim(this._$input.val());
        if (q) {
            var query = $form.attr('action') + '?' + $form.serialize();
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
    },

    /**
     * @param {Event} e
     */
    _onCheckboxClick: function (e) {
        var $this = $(e.currentTarget);
        this._changeCheckbox($this);
        $(e.target).blur();
        return false;
    },

    /**
     * @param {jQuery} $element
     */
    _changeCheckbox: function ($element) {
        var $checkbox = $element.find('input[type = checkbox]');
        $checkbox.attr('checked', !$checkbox.attr('checked'));
        $checkbox.trigger('change');
        $element.toggleClass('checked', Boolean($checkbox.attr('checked')));
    }
};

})();
