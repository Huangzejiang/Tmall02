let shops_url = 'http://127.0.0.1:8000/home/shop/';
let IMG_URL = 'http://127.0.0.1:8000/static/img/productSingle_middle/';
$(function () {
    $.get(shops_url, function (result) {
        if (null != result && result.state === 200 && result.data.length > 0) {
            let $content = $('#content');
            for (let cate of result.data) {
                //每一项的div
                let $div = $('<div>');
                //给div添加在元素
                //创建分类标题
                let $h3 = $('<h3>').text(cate.name);
                //创建ul
                let $ul = $('<ul>').attr('class', 'clear');
                if (cate.products.length > 0) {
                    for (let product of cate.products) {
                        //创建li元素
                        let $li = $('<li>');
                        //
                        let $a = $('<a>');
                        //给a标签添加img元素
                        $a.append($('<img>').attr('src', IMG_URL + product.imgs[0].id + '.jpg'))
                            .append($('<span>').text(product.name))
                            .append($('<span>').text(product.promote_price));
                        //将a标签添加到li中
                        $li.append($a);
                        $ul.append($li)
                    }
                }
                /**
                 * 1.查找最外层的div
                 * 2 子div添加到外层的div
                 * 3.把h3 添加到子div
                 * 4.把ul添加到子div
                 */
                $('#content').append($div.append($h3).append($ul));
            }
        }
    })
})

