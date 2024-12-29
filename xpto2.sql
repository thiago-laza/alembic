-- Running downgrade 70be69d705e5 -> 4509f3478aee

ALTER TABLE pessoa2 DROP COLUMN idade;

UPDATE alembic_version SET version_num='4509f3478aee' WHERE alembic_version.version_num = '70be69d705e5';

-- Running downgrade 4509f3478aee -> 8a75358ecf69

DROP TABLE pessoa2;

UPDATE alembic_version SET version_num='8a75358ecf69' WHERE alembic_version.version_num = '4509f3478aee';

