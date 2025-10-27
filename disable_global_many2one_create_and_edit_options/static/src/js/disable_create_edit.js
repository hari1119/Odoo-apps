/** @odoo-module **/

import { patch } from '@web/core/utils/patch';
import { Many2OneField } from '@web/views/fields/many2one/many2one_field';

patch(Many2OneField.prototype, {
    setup() {
        super.setup();

        // Override props directly
        const props = this.props;
        if (props) {
            props.canCreate = false;
            props.canCreateEdit = false;
            props.canQuickCreate = false;
            props.canWrite = false;
        }
    },
});

