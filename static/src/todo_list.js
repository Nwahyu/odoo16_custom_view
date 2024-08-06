/** @odoo-module **/

import { registry } from "@web/core/registry";
const { Component, useState } = owl;


export class OwlTodoList extends Component {
    setup() {
        this.state = useState({value:1})
    }
}

OwlTodoList.template = 'tes_satu.TodoListTemplate'
registry.category('actions').add('tes_satu.action_todo_list_js', OwlTodoList);