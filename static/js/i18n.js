(function () {

$(document).ready(init);

function init() {
    new I18n();
}

function I18n() {
    this._$form = $('.i18n-form');
    this._$button = this._$form.find('button');

    this._addEventListeners();
}

I18n.prototype = {
    /**
     * Добавляем события.
     */
    _addEventListeners: function () {
        this._$button.on({
            click: this._onButtonClick.bind(this)
        });
    },

    /**
     * @param {Event} e
     */
    _onButtonClick: function (e) {
        var $this = $(e.currentTarget);
        var forId = $this.data('for');
        this._$form.find('#' + forId).click();
        this._$form.submit();
    }
};

})();
