(function () {

$(document).ready(init);

/**
 * Такой же как в settings.py.
 * @type {string}
 */
var FILTER_KEY = 'filter';

function parseQuery() {
    var query = {};
    window.location.search.substring(1).split('&').forEach(function (param) {
        var params = param.split('=');
        query[decodeURIComponent(params[0])] = decodeURIComponent(params[1]);
    });
    return query;
}

function stringifyQuery(query, removeKeys) {
    removeKeys.forEach(function (key) {
        delete query[key];
    });
    return '?' + Object.keys(query).map(function (key) {
        return encodeURIComponent(key) + '=' + encodeURIComponent(query[key]);
    }).join('&');
}

function init() {
    new Competitions();
}

function Competitions() {
    this._$filters = $('.competition-filter a');

    this._updateFilter();
    this._addEventListeners();
}

Competitions.prototype = {
    _addEventListeners: function () {},

    _updateFilter: function () {
        var query = parseQuery();

        this._$filters.each(function (index) {
            var $link = this._$filters.eq(index);
            query[FILTER_KEY] = $link.data(FILTER_KEY);
            var search = stringifyQuery(query, ['page']);
            $link.attr('href', window.location.pathname + search);
        }.bind(this));
    }
};

})();
