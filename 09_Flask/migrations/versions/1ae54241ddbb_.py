"""empty message

Revision ID: 1ae54241ddbb
Revises: 
Create Date: 2022-03-25 23:52:32.317463

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1ae54241ddbb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dept',
    sa.Column('dno', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('dno')
    )
    # op.drop_index('auth_user_user_permissions_user_id_permission_id_14a6b632_uniq', table_name='auth_user_user_permissions')
    # op.drop_table('auth_user_user_permissions')
    # op.drop_index('django_session_expire_date_a5c62663', table_name='django_session')
    # op.drop_table('django_session')
    # op.drop_index('name', table_name='auth_group')
    # op.drop_table('auth_group')
    # op.drop_index('auth_user_groups_user_id_group_id_94350c0c_uniq', table_name='auth_user_groups')
    # op.drop_table('auth_user_groups')
    # op.drop_table('django_migrations')
    # op.drop_table('django_admin_log')
    # op.drop_index('username', table_name='auth_user')
    # op.drop_table('auth_user')
    # op.drop_table('teacher')
    # op.drop_index('django_content_type_app_label_model_76bd3d3b_uniq', table_name='django_content_type')
    # op.drop_table('django_content_type')
    # op.drop_index('name', table_name='peopleinfo')
    # op.drop_table('peopleinfo')
    # op.drop_index('auth_group_permissions_group_id_permission_id_0cd325b0_uniq', table_name='auth_group_permissions')
    # op.drop_table('auth_group_permissions')
    # op.drop_index('name', table_name='bookinfo')
    # op.drop_table('bookinfo')
    # op.drop_index('auth_permission_content_type_id_codename_01ab375a_uniq', table_name='auth_permission')
    # op.drop_table('auth_permission')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('auth_permission',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('content_type_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('codename', mysql.VARCHAR(length=100), nullable=False),
    sa.ForeignKeyConstraint(['content_type_id'], ['django_content_type.id'], name='auth_permission_content_type_id_2f476e4b_fk_django_co'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_index('auth_permission_content_type_id_codename_01ab375a_uniq', 'auth_permission', ['content_type_id', 'codename'], unique=False)
    op.create_table('bookinfo',
    sa.Column('id', mysql.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('pub_date', sa.DATE(), nullable=True),
    sa.Column('readcount', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('commentcount', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('is_delete', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_index('name', 'bookinfo', ['name'], unique=False)
    op.create_table('auth_group_permissions',
    sa.Column('id', mysql.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('group_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('permission_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['auth_group.id'], name='auth_group_permissions_group_id_b120cbf9_fk_auth_group_id'),
    sa.ForeignKeyConstraint(['permission_id'], ['auth_permission.id'], name='auth_group_permissio_permission_id_84c5c92e_fk_auth_perm'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_index('auth_group_permissions_group_id_permission_id_0cd325b0_uniq', 'auth_group_permissions', ['group_id', 'permission_id'], unique=False)
    op.create_table('peopleinfo',
    sa.Column('id', mysql.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('gender', mysql.SMALLINT(), autoincrement=False, nullable=False),
    sa.Column('description', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('is_delete', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.Column('book_id', mysql.BIGINT(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['bookinfo.id'], name='peopleinfo_book_id_8d70a162_fk_bookinfo_id'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_index('name', 'peopleinfo', ['name'], unique=False)
    op.create_table('django_content_type',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('app_label', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('model', mysql.VARCHAR(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_index('django_content_type_app_label_model_76bd3d3b_uniq', 'django_content_type', ['app_label', 'model'], unique=False)
    op.create_table('teacher',
    sa.Column('tid', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=100), nullable=False),
    sa.PrimaryKeyConstraint('tid'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_table('auth_user',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('password', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('last_login', mysql.DATETIME(fsp=6), nullable=True),
    sa.Column('is_superuser', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.Column('username', mysql.VARCHAR(length=150), nullable=False),
    sa.Column('first_name', mysql.VARCHAR(length=150), nullable=False),
    sa.Column('last_name', mysql.VARCHAR(length=150), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=254), nullable=False),
    sa.Column('is_staff', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.Column('is_active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.Column('date_joined', mysql.DATETIME(fsp=6), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_index('username', 'auth_user', ['username'], unique=False)
    op.create_table('django_admin_log',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('action_time', mysql.DATETIME(fsp=6), nullable=False),
    sa.Column('object_id', mysql.LONGTEXT(), nullable=True),
    sa.Column('object_repr', mysql.VARCHAR(length=200), nullable=False),
    sa.Column('action_flag', mysql.SMALLINT(unsigned=True), autoincrement=False, nullable=False),
    sa.Column('change_message', mysql.LONGTEXT(), nullable=False),
    sa.Column('content_type_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.CheckConstraint('(`action_flag` >= 0)', name='django_admin_log_chk_1'),
    sa.ForeignKeyConstraint(['content_type_id'], ['django_content_type.id'], name='django_admin_log_content_type_id_c4bce8eb_fk_django_co'),
    sa.ForeignKeyConstraint(['user_id'], ['auth_user.id'], name='django_admin_log_user_id_c564eba6_fk_auth_user_id'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_table('django_migrations',
    sa.Column('id', mysql.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('app', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('applied', mysql.DATETIME(fsp=6), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_table('auth_user_groups',
    sa.Column('id', mysql.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('group_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['auth_group.id'], name='auth_user_groups_group_id_97559544_fk_auth_group_id'),
    sa.ForeignKeyConstraint(['user_id'], ['auth_user.id'], name='auth_user_groups_user_id_6a12ed8b_fk_auth_user_id'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_index('auth_user_groups_user_id_group_id_94350c0c_uniq', 'auth_user_groups', ['user_id', 'group_id'], unique=False)
    op.create_table('auth_group',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_index('name', 'auth_group', ['name'], unique=False)
    op.create_table('django_session',
    sa.Column('session_key', mysql.VARCHAR(length=40), nullable=False),
    sa.Column('session_data', mysql.LONGTEXT(), nullable=False),
    sa.Column('expire_date', mysql.DATETIME(fsp=6), nullable=False),
    sa.PrimaryKeyConstraint('session_key'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_index('django_session_expire_date_a5c62663', 'django_session', ['expire_date'], unique=False)
    op.create_table('auth_user_user_permissions',
    sa.Column('id', mysql.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('permission_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['permission_id'], ['auth_permission.id'], name='auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm'),
    sa.ForeignKeyConstraint(['user_id'], ['auth_user.id'], name='auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_index('auth_user_user_permissions_user_id_permission_id_14a6b632_uniq', 'auth_user_user_permissions', ['user_id', 'permission_id'], unique=False)
    op.drop_table('dept')
    # ### end Alembic commands ###