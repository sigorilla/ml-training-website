(function () {

$(document).ready(init);

function init() {
    new Competitions();
}

function Competitions() {
    this._$competitions = $('.competition-item');
    this._$showMore = $('.competition-item .show-more');
    this._addEventListeners();
}

Competitions.prototype = {
    _addEventListeners: function () {
        this._$competitions.find('.more-information').hide().removeClass('hidden');
        this._$showMore.on({
            click: this._onClickShowMore.bind(this)
        });
    },

    /**
     * @param {Event} e
     */
    _onClickShowMore: function (e) {
        e.preventDefault();
        $(e.currentTarget).parents('.competition-item').find('.more-information').toggle(300);
    }
};

})();
